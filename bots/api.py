import tweepy
import configparser
from github import Github

def readGithubAPIConfig(loc):
    config = configparser.ConfigParser()
    config.read(loc)
    return {
        "token" : config.get("GITHUB", "token"),
        }

def createGitHubAPI(cfgloc = "~/.rse2_d2.ini"):
    cfg = reactGithubAPIConfig(cfgloc)
    return Github(cfg["token"])

def readTwitterAPIConfig(loc):
    config = configparser.ConfigParser()
    config.read(loc)
    # TODO: Error handling when key/secret does not exist
    return {
        "ckey" : config.get("TWITTER", "consumer_key"),
        "csecret" : config.get("TWITTER", "consumer_secret"),
        "akey" : config.get("TWITTER", "access_key"),
        "asecret" : config.get("TWITTER", "access_secret")
       }

def createTwitterAPI(cfgloc = "~/.rse2_d2.ini"):
    cfg = readTwitterAPIConfig(cfgloc)
    auth = tweepy.OAuthHandler(cfg["ckey"], cfg["csecret"])
    auth.set_access_token(cfg["akey"],cfg["asecret"])
    tapi = tweepy.API(auth)
    try:
      tapi.verify_credentials()
    except Exception as e:
      print("Error creating twitter API")
      raise e
    print("Twitter API Created")
    return tapi
