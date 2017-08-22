import os
import urllib.parse
import base64
import requests

def obtain_bearer_token():
    rq = requests.post("https://api.twitter.com/oauth2/token",
                       headers={"Authorization": "Basic {}".format(_encode_keys()),
                                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
                       data="grant_type=client_credentials")

    response = rq.json()
    assert "bearer" == response["token_type"]
    return response["access_token"]

def _encode_keys():
    consumer = urllib.parse.quote_plus(os.environ["CONSUMER_KEY"])
    secret = urllib.parse.quote_plus(os.environ["CONSUMER_SECRET"])
    concatenated = "{}:{}".format(consumer, secret).encode()
    return base64.b64encode(concatenated).decode()


TOKEN = obtain_bearer_token()

def get_json(tweet_id, **kwargs):
    params = {"id": tweet_id,
              "trim_user": kwargs.get("trim_user", "false"),
              "include_entities": kwargs.get("include_entities", "true")}
    rq = requests.get("https://api.twitter.com/1.1/statuses/show.json",
                      headers={"Authorization": "Bearer {}".format(TOKEN)},
                      params=params)
    return rq.json()
