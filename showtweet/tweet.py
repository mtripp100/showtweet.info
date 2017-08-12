import os
import urllib.parse
import base64
import requests

def get_json(tweet_id):
    return "{} - nothing to see here...".format(tweet_id)

def obtain_bearer_token():
    rq = requests.post("https://api.twitter.com/oauth2/token", headers={'Authorization': "Basic {}".format(_encode_keys()),
                                                                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'},
                       data='grant_type=client_credentials')
    response = rq.text
    assert 'bearer' == response['token_type']
    return response['access_token']

def _encode_keys():
    consumer = urllib.parse.quote_plus(os.environ['CONSUMER_KEY'])
    secret = urllib.parse.quote_plus(os.environ['CONSUMER_SECRET'])
    concatenated = "{}:{}".format(consumer, secret).encode()
    return base64.b64encode(concatenated).decode()