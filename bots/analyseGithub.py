import api
import argparse
import re

def analyseGithubLinkAndRespond(api, link):
    print("Unimplemented")

def containsGitHubURL(s) :
    return "github.com/" in s

# TODO: Error handling - assumes we find a link
def extractGitHubLink(s) :
    matches = re.findall(r'(https?://github.com/\S+)', s)
    return matches[0]

def getMentions(api, lastId):
    latestId = lastId
    for tweet in tweepy.Cursor(api.mentions_timeline,
                            since_id=lastId).items():
        latestId = max(latestId, tweet.id)
        if containsGitHubURL(tweet.text.lower()):
            analyseGithubLinkAndRespond(api, extractGitHubLink(latestId))

def main():
    parser = argparse.ArgumentParser(description='RSE2-D2 github analysing bot.')
    parser.add_argument('--config', nargs='?',
                        help='Location of the local API config file')
    args = parser.parse_args()

    cfgloc = ""
    if args.config != None:
        cfgloc = args.config
        # TODO: Also check the file exists

    print("Creating API with config location:" + cfgloc)

    api.createAPI(cfgloc)

if __name__ == "__main__":
    main()
