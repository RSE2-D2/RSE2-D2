import argparse
import time

import api
import tweeter


def main():
    parser = argparse.ArgumentParser(description='RSE2-D2 github analysing bot.')
    parser.add_argument('--config', nargs='?',
                        help='Location of the local API config file')
    args = parser.parse_args()

    cfgloc = ""
    if args.config is not None:
        cfgloc = args.config
        # TODO: Also check the file exists

    print("Creating API with config location:" + cfgloc)

    twitter = api.createTwitterAPI(cfgloc)

    while True:
        print("Sending tweet...",)
        tweeter.sendTweet(twitter)
        print("Sent.")
        time.sleep(86400)


if __name__ == "__main__":
    main()
