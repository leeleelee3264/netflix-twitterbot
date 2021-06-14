# Project: twitter_project
# Author: absin
# Date: 2021-03-25
# DESC:
# Project: twitter_project
# Author: absin
# Date: 2021-03-24
# DESC:
import tweepy
import os
from pathlib import Path
import regex
import util


# key mapping
_API_KEY = 'TWITTER_API_KEY'
_API_KEY_SECRET = 'TWITTER_API_SECRET'
_ACCESS_TOKEN = 'TWITTER_ACCESS_TOKEN'
_ACCESS_TOKEN_SECRET = 'TWITTER_ACCESS_TOKEN_SECRET'


def OAuth():
    try:
        api_key = os.environ.get(_API_KEY)
        api_key_secret = os.environ.get(_API_KEY_SECRET)

        access_token = os.environ.get(_ACCESS_TOKEN)
        access_token_secret = os.environ.get(_ACCESS_TOKEN_SECRET)

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


# OAuth 와는 다르게 내부에 키 정보를 가지고 있다
def inner_OAuth(key_hash: dict):
    try:
        api_key = key_hash[_API_KEY]
        api_key_secret = key_hash[_API_KEY_SECRET]

        access_token = key_hash[_ACCESS_TOKEN]
        access_token_secret = key_hash[_ACCESS_TOKEN_SECRET]

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        return auth
    except KeyError as e:
        print(e)
        return None


def post_tweet(container: dict, date):
    oauth = OAuth()
    api = tweepy.API(oauth)
    _current_dir = os.path.dirname(os.path.abspath(__file__))
    _path = Path(_current_dir)

    BASE_DIR = _path.parent.absolute()
    IMG_DIR = f'{BASE_DIR}/img/netflix/{date}'

    for key in container:
        tTitle = key
        tFile = f'{IMG_DIR}/{tTitle}.png'
        print(f'{tFile}')
        reTitle = regex.change_hyphen(tTitle)

        tweet_format = f'[{reTitle}]\n 공개 예정일:{container[key]}'
        api.update_with_media(tFile, status=tweet_format)



def post_tweet_list(container: list, img_dir, keys : dict ):
    oauth = inner_OAuth(keys)
    api = tweepy.API(oauth)
    IMG_DIR = img_dir

    if not container:
        return None

    index = len(container) - 1

    while index >= 0:
        tInfo = container[index]
        tImg = f'{IMG_DIR}/{index}.png'

        api.update_with_media(tImg, status=tInfo)

        index = index - 1
