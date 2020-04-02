import api
import argparse
import json
import os
import random
import time

JSON_KEY_GENERAL = 'general'
JSON_KEY_QUOTE = 'quote'
JSON_KEY_RANDOM = 'randomiser'


def getTweet(jsonFilename, section=JSON_KEY_GENERAL, reply_username=None):
    # TODO: Load only once - refresh every now and then
    with open(jsonFilename) as dbfile:
        data = json.load(dbfile)
        dbfile.close()

    tweets = data.get(section)

    if len(tweets) > 0:
        tweet = random.choice(tweets).get(JSON_KEY_QUOTE)

        random_words = data.get(JSON_KEY_RANDOM)
        start = random.choice(random_words)
        end = random.choice(random_words)
        tweet = ' '.join([start, tweet, end])

        if reply_username is not None:
            tweet = '@' + reply_username + ' ' + tweet

    return tweet


def sendTweet(twitter_api, jsonFilename, section=JSON_KEY_GENERAL):
    newTweet = getTweet(jsonFilename, section)
    twitter_api.update_status(newTweet)
