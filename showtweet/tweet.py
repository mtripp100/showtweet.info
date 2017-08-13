import os
import urllib.parse
import base64
import requests
import socket

def obtain_bearer_token():
    rq = requests.post("https://api.twitter.com/oauth2/token", headers={'Authorization': "Basic {}".format(_encode_keys()),
                                                                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'},
                       data='grant_type=client_credentials')
    response = rq.json()
    assert 'bearer' == response['token_type']
    return response['access_token']

def _encode_keys():
    consumer = urllib.parse.quote_plus(os.environ['CONSUMER_KEY'])
    secret = urllib.parse.quote_plus(os.environ['CONSUMER_SECRET'])
    concatenated = "{}:{}".format(consumer, secret).encode()
    return base64.b64encode(concatenated).decode()

TOKEN = obtain_bearer_token()

def get_json(tweet_id, **kwargs):
    params = {"id": tweet_id,
              "trim_user": "false" if "include_users" in kwargs else "true",
              "include_entities": "true" if "include_entities" in kwargs else "false"}
    rq = requests.get("https://api.twitter.com/1.1/statuses/show.json",
                      headers={"Authorization": "Bearer {}".format(TOKEN)},
                      params=params)
    record_metrics(rq.headers)
    return rq.json()

def record_metrics(headers):
    rate_metric = "{}.rate_limit {}\n".format(os.environ['HOSTEDGRAPHITE_APIKEY'], headers['x-rate-limit-remaining'])

    conn = socket.create_connection(("efc43c1b.carbon.hostedgraphite.com", 2003))
    conn.send(rate_metric.encode())
    conn.close()
