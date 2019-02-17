import os

USER_MAP = {
    'GlobalEntry': {
        'username': os.environ.get("TWITTER_USERNAME"),
        'password': os.environ.get("TWITTER_PASSWORD"),
    },
}


class Path:
    CONFIG = "config.yml"
    FAILED_SCREENSHOT = "./failed_scenarios_screenshots/"


class URL:
    TWITTER = 'https://twitter.com'


class Constants:
    USERNAME = 'username'
    GLOBAL_ENTRY_Q = '#globalentry'
    TWEETS = 'tweets'
