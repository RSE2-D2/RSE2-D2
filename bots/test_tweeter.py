import os

import tweeter

ERROR_JSON = os.path.join(os.path.dirname(os.path.realpath(__file__)), "advice_db.json")


def test_getGeneralTweet():
    tweet = tweeter.getTweet(ERROR_JSON)
    assert(type(tweet) == str)
    assert(len(tweet) > 0)


def test_getSectionTweet():
    tweet = tweeter.getTweet(ERROR_JSON, "NoLicense", 'RSE2_D2')
    assert(tweet == "@RSE2_D2 Facing all that you fear will free you from yourself. Decide on a license you must.")
