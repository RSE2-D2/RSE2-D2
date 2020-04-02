import api
import argparse
import json
import os
import random
import time

JSON_KEY_GENERAL = 'general'
JSON_KEY_QUOTE = 'quote'


def getTweet(section=JSON_KEY_GENERAL):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(current_dir, "advice_db.json")) as dbfile:
        data = json.load(dbfile)
        general_tweets = data.get(JSON_KEY_GENERAL)
        tweet = random.choice(general_tweets).get(JSON_KEY_QUOTE)
        dbfile.close()

    return tweet


def sendTweet(twitter_api, section=JSON_KEY_GENERAL):
    newTweet = getTweet(section)
    twitter_api.update_status(newTweet)
