import api
import argparse
import re

import tweepy

files_we_need = {
    "readme" : ["readme", "README", "README.md",
                "readme.md", "readme.rst", "README.rst"]
}

def analyseGithubLinkAndRespond(github, twitter, link):
    repo = github.get_repo(link)

    contents = repo.get_contents("")
    for content_file in contents:
        print(content_file)

    print(files_we_need["readme"])

def containsGitHubURL(s) :
    return "github.com/" in s

# TODO: Error handling - assumes we find a link
def extractGitHubLink(s) :
    matches = re.findall(r'(https?://github.com/\S+)', s)
    repo = re.sub(r'https?://github.com/', "", matches[0])
    return repo

def watchMentions(github, twitter, lastId):
    latestId = lastId
    for tweet in tweepy.Cursor(api.mentions_timeline,
                            since_id=lastId).items():
        latestId = max(latestId, tweet.id)
        if containsGitHubURL(tweet.text.lower()):
            analyseGithubLinkAndRespond(twitter, extractGitHubLink(latestId))

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

    twitter = api.createAPI(cfgloc)
    github = api.createGitHubApi(cfgloc)
    #
    # TODO: Will this get all tweats in history? Might need to scan for the most recent first?
    initialId = 1
    while True:
        watchMentions(github, twitter, initalId)
        sleep(30)

if __name__ == "__main__":
    main()
