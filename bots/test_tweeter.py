import tweeter


def test_getTweet():
    tweet = tweeter.getTweet()
    assert(type(tweet) == str)
    assert(len(tweet) > 0)
