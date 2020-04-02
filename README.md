# RSE2-D2
RSE2-D2 Twitter bot - Providing helpful advice for research software 

![RSE2-D2](https://mir-s3-cdn-cf.behance.net/project_modules/disp/9c2f1f9986639.560dd95e62864.png)

## Setup

It's probably helpful to use [virtualenv](https://virtualenv.pypa.io) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) to manage your environment.

Once you have them installed, create a new environment:

```mkvirtualenv --python=python3.7 RSE2-D2```

Then install the requirements:

```pip install -r requirements.txt```

Currently we're using [tweepy](http://tweepy.readthedocs.org) for interacting with Twitter and [pygithub](https://pygithub.readthedocs.io) to interact with GitHub.

## Running the AnalyseGithub Bot

The analyseGithub RSE2-D2 bot can be run as:

```python bots/analyseGithub.py ```

Twitter credentials are read from the ini file of the form:

[TWITTER]
consumer_key:
consumer_secret:
access_key:
access_secret:

At either: ~/.rse2_d2.ini or at the location given by "--config"
