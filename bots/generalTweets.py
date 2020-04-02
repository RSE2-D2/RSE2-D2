import api
import argparse
import re
import json
import random

import tweepy

def getTweet():
    with open("./advice_db.json") as dbfile:
        data = json.load(dbfile)
        # get string from file
        whichTweet = random.randint(0, len(data.general)) # make this random
	tweet = data.general[whichTweet].quote
	return tweet
    

def main():
# No idea what of this I need
    parser = argparse.ArgumentParser(description='RSE2-D2 github analysing bot.')
    parser.add_argument('--config', nargs='?',
                        help='Location of the local API config file')
    args = parser.parse_args()

    cfgloc = ""
    if args.config != None:
        cfgloc = args.config
        # TODO: Also check the file exists

    print("Creating API with config location:" + cfgloc)

    twitter = api.createAPI(cfgloc)
    latestId = 1
    while True:
	newTweet = getTweet();
        twitter.update_status(newTweet)
        sleep(86400)

if __name__ == "__main__":
    main()
