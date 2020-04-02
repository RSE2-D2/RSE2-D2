# RSE2-D2
RSE2-D2 Twitter bot - Providing helpful advice for research software 

![RSE2-D2](https://mir-s3-cdn-cf.behance.net/project_modules/disp/9c2f1f9986639.560dd95e62864.png)

## Setup

It's probably helpful to use [virtualenv](https://virtualenv.pypa.io) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) to manage your environment.

Once you have them installed, create a new environment:

```mkvirtualenv --python=python3.7 RSE2-D2```

Then install the requirements:

```pip install -r requirements.txt```

Currently we're using [tweepy](http://tweepy.readthedocs.org) for interacting
with Twitter and [pygithub](https://pygithub.readthedocs.io) to interact with
GitHub. To use these you will first need to generate API tokens as described
here for
[Twitter](https://developer.twitter.com/en/docs/basics/authentication/overview)
and
[Github](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).

## Running the AnalyseGithub Bot

The analyseGithub RSE2-D2 bot can be run as:

```python bots/analyseGithub.py ```

The bot will read API tokens from either: ~/.rse2_d2.ini or at the location
given by "--config".

An example API configuration ini file is in `api_config.ini`.

The local database of responses is given by the argument ```--error_json```

For example, we can run with a local config and default responses with

```python bots/analyseGithub.py --config api_config.ini --error_json bots/advice/db.json```
