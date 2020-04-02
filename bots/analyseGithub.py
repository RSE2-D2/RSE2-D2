import api
import argparse
import re
import time
import requests
import random
import json

import tweepy

### Filenames we want to see present
# To add another file type use this template schema
#     "filetypeDescription" : {
#        "filenames" : ["file.md", "FILE", "permutation3"],
#        "error" : "errorname_from_advice_db.json"
#    }


files_we_need = { #Use casefold() for case insensitive comparison
    "readme" : {
    "filenames" : ["readme", "readme.md", "readme.rst", "readme.txt"],
    "error" :"NoReadMe"
    },
    "license" : {
        "filenames" : ["license", "license.md", "license.rst", "license.txt"],
        "error" : "NoLicense"
    },
    "codeofconduct" : {
        "filenames" : ["code_of_conduct", "codeofconduct", "code_of_conduct.md", "codeofconduct.md", "code_of_conduct.rst", "codeofconduct.rst"  "code_of_conduct.txt", "codeofconduct.txt"],
        "error" : "NoCodeOfConduct"
    }
# Add more files from https://github.com/joelparkerhenderson/github_special_files_and_paths ?
}


def analyseGithubLinkAndRespond(github, twitter, errorJSON, tweet, link):
    repo = ();
    try:
        repo = github.get_repo(link)
    except Exception as e:
        print(e)
        return

    # gather all files in the root of the repo
    contents = repo.get_contents("")
    contents_files_lowercase = []

    for content in contents:
        contents_files_lowercase.append(content.name.casefold())

    print("contents of repo root:")
    print(contents_files_lowercase)



    missing = []
    #iterate through approved file list and for each type, check if it's present
    for a_file_type in files_we_need:
        the_type = files_we_need[a_file_type]
        print("--> checking for " + a_file_type);
        # check for intersection in existing file namesand possible file names
        found = set(contents_files_lowercase).intersection(the_type["filenames"])
        if len(found) > 0:
            print("|------ found " + a_file_type)
        else:
            print("|xx-notfound " + a_file_type)
            missing.append(the_type["error"])

    # Send a tweet for something we are lacking faith in
    if len(missing) > 0:
        f = random.choice(missing)
        print("tweeting about: " + f)
        # TODO: Load only once - refresh every now and then
        responseDB = {}
        with open(errorJSON) as db:
            responseDB = json.load(db)

        possibleResponses = responseDB.get(f, [])
        if len(possibleResponses) > 0:
            responseTxt = random.choice(possibleResponses)
            res = "@" + tweet.user.screen_name + " " + responseTxt["quote"]
            print("Responding with:" + res)
            print("Replying to id" + str(tweet.id))
            twitter.update_status(
                status=" " + res,
                in_reply_to_status_id=tweet.id,
            )

    return


def analyseGithubLinkAndRespond_CI(github, twitter, link):
    repo = github.get_repo(link)

    branch = repo.get_branch(repo.default_branch)
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

def watchMentions(github, twitter, errorJSON, lastId):
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
                analyseGithubLinkAndRespond(github, twitter, errorJSON, tweet, extractGitHubLink(link))

    return latestId

def main():
    parser = argparse.ArgumentParser(description='RSE2-D2 github analysing bot.')
    parser.add_argument('--config', nargs='?',
                        help='Location of the local API config file')
    parser.add_argument('--error_json', required=True, help='Location of the local JSON response DB')
    args = parser.parse_args()

    cfgloc = ""
    if args.config != None:
        cfgloc = args.config
        # TODO: Also check the file exists

    print("Creating API with config location:" + cfgloc)

    twitter = api.createTwitterAPI(cfgloc)
    github = api.createGitHubAPI(cfgloc)

    latestId = 1245701334373892130
    while True:
        latestId = watchMentions(github, twitter, args.error_json, latestId)
        time.sleep(30)

if __name__ == "__main__":
    main()
