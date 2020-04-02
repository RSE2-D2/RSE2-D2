import tweepy
import configparser

def readAPIConfig(loc):
    config = configparser.ConfigParser()
    config.read(loc)
    # TODO: Error handling when key/secret does not exist
    return {
        "ckey" : config.get("TWITTER", "consumer_key"),
        "csecret" : config.get("TWITTER", "consumer_secret"),
        "akey" : config.get("TWITTER", "access_key"),
        "asecret" : config.get("TWITTER", "access_secret")
       }

def createAPI(cfgloc = "~/.rse2_d2.ini"):
    cfg = readAPIConfig(cfgloc)
    auth = tweepy.OAuthHandler(cfg["ckey"], cfg["csecret"])
    auth.set_access_token(cfg["akey"],cfg["asecret"])
    tapi = tweepy.API(auth)
    try:
      tapi.verify_credentials()
    except Exception as e:
      print("Error creating API")
      raise e
    print("API Created")
    return tapi
