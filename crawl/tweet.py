# Project: twitter_project
# Author: absin
# Date: 2021-03-24
# DESC:
import tweepy
import os


def OAuth():
    try:
        api_key = os.environ.get('TWITTER_API_KEY')
        api_key_secret = os.environ.get('TWITTER_API_KEY_SECRET')

        auth = tweepy.OAuthHandler()
