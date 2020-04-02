import argparse
import time

import api
import tweeter


def main():
    parser = argparse.ArgumentParser(description='RSE2-D2 github analysing bot.')
    parser.add_argument('--config', nargs='?',
                        help='Location of the local API config file')
    parser.add_argument('--error_json', help='Location of the local JSON response DB')
    args = parser.parse_args()

    cfgloc = ""
    if args.config is not None:
        cfgloc = args.config
        # TODO: Also check the file exists

    print("Creating API with config location:" + cfgloc)
    print("Using JSON file from:" + args.error_json)

    twitter = api.createTwitterAPI(cfgloc)

    while True:
        print("Sending tweet...",)
        tweeter.sendTweet(twitter, args.error_json)
        print("Sent.")
        time.sleep(86400)


if __name__ == "__main__":
    main()
