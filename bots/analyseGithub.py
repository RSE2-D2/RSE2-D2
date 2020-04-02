import api
import argparse
import re
import time
import requests

import tweepy

files_we_need = {
    "readme" : ["readme", "README", "README.md",
                "readme.md", "readme.rst", "README.rst"]
}

def analyseGithubLinkAndRespond(github, twitter, link):
    repo = ();
    try:
        repo = github.get_repo(link)
    except Exception as e:
        return

    contents = repo.get_contents("")
    for content_file in contents:
        print(content_file)

    print(files_we_need["readme"])

def analyseGithubLinkAndRespond_CI(github, twitter, link):
    repo = github.get_repo(link)

    branch = repo.get_branch("master") # FIXME get the default branch instead of master
    last_commit = branch.commit
    checks = last_commit.get_combined_status()
    if checks.total_count:
        # Are they passing?
        if checks.state == "success":
            print(f"You've got {checks.total_count} checks in place and all are passing!")
        else:
            passing = sum([a.state == "success" for a in checks.statuses])
            print(f"You've got {passing} checks from  {checks.total_count}! You are in a right track!")
    else:
        print("You need some checks!")


def containsGitHubURL(s) :
    return "github.com/" in s

def containsTwitterURL(s) :
    return "t.co/" in s

def checkURLForGitHubLink(url) :
    loc = requests.head(url + "?amp=1").headers['location']
    if containsGitHubURL(loc):
        return loc
    else:
        return ""

# TODO: Error handling - assumes we find a link
def extractGitHubLink(s) :
    matches = re.findall(r'(https?://github.com/\S+)', s)
    repo = re.sub(r'https?://github.com/', "", matches[0])
    return repo

def extractURL(s) :
    matches = re.findall(r'(https?://t.co/\S+)', s)
    return matches[0]

def watchMentions(github, twitter, lastId):
    latestId = lastId
    for tweet in tweepy.Cursor(twitter.mentions_timeline,
                            since_id=latestId).items():
        latestId = max(latestId, tweet.id)
        print("Found new tweet")
        print("Tweet content:" + tweet.text.lower())
        if containsTwitterURL(tweet.text.lower()):
            print("Got a URL. Analysing")
            link = checkURLForGitHubLink(extractURL(tweet.text))
            if link != "":
                print("Got github. Analysing")
                analyseGithubLinkAndRespond(github, twitter, extractGitHubLink(link))

    return latestId

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

    twitter = api.createTwitterAPI(cfgloc)
    github = api.createGitHubAPI(cfgloc)
  
    latestId = 1245666650088714251
    while True:
        latestId = watchMentions(github, twitter, latestId)
        time.sleep(30)

if __name__ == "__main__":
    main()
