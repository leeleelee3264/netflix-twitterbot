# Project: twitter_project
# Author: absin
# Date: 2021-03-24
# DESC:
import tweepy
import os


def OAuth():
    try:
        api_key = os.environ.get('TWITTER_API_KEY')
        api_key_secret = os.environ.get('TWITTER_API_SECRET')

        access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None



def postTweet(container: dict):
    oauth = OAuth()
    api = tweepy.API(oauth)

    # TODO: 여기다가 이미지 넣는 방법 찾아야 한다
    for key in container:
        tweet_format = f'[{key}]\n 공개 여정일:{container[key]}'
        api.update_status(tweet_format)




