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
API_KEY = 'TWITTER_API_KEY'
API_KEY_SECRET = 'TWITTER_API_SECRET'
ACCESS_TOKEN = 'TWITTER_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'TWITTER_ACCESS_TOKEN_SECRET'


def OAuth():
    try:
        api_key = os.environ.get(API_KEY)
        api_key_secret = os.environ.get(API_KEY_SECRET)

        access_token = os.environ.get(ACCESS_TOKEN)
        access_token_secret = os.environ.get(ACCESS_TOKEN_SECRET)

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


# OAuth 와는 다르게 내부에 키 정보를 가지고 있다
def inner_OAuth(key_hash: dict):
    try:
        api_key = key_hash[API_KEY]
        api_key_secret = key_hash[API_KEY_SECRET]

        access_token = key_hash[ACCESS_TOKEN]
        access_token_secret = key_hash[ACCESS_TOKEN_SECRET]

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
        tTile_without_white = regex.change_whitespace(tTitle, '_')
        tTtile_without_speical = regex.change_file_disable(tTile_without_white)
        tFile = f'{IMG_DIR}/{tTtile_without_speical}.png'
        print(f'{tFile}')

        tweet_format = f'[{tTitle}]\n 공개 예정일:{container[key]}'
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


def post_tweet_img_di(img_obj, fmt,  keys: dict):
    """
    This function get received img object from caller.
    Before this func, caller only passes path of img in server.
    """

    oauth = inner_OAuth(keys)
    api = tweepy.API(oauth)

    api.update_with_media(img_obj, status=fmt)