import api
import argparse
import re
import time
import requests

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

def analyseGithubLinkAndRespond(github, twitter, link):
    repo = ();
    try:
        repo = github.get_repo(link)
    except Exception as e:
        return

    # gather all files in the root of the repo
    contents = repo.get_contents("")

    # iterate through approved file list and for each type, check if it's present
    for a_file_type in files_we_need:
        the_type = files_we_need[a_file_type]
        for filename_option in the_type["filenames"]:
            print(filename_option)

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
