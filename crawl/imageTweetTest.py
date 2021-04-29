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


def post_tweet(container: dict, date):
    oauth = OAuth()
    api = tweepy.API(oauth)
    _current_dir = os.path.dirname(os.path.abspath(__file__))
    _path = Path(_current_dir)

    BASE_DIR = _path.parent.absolute()
    IMG_DIR = f'{BASE_DIR}/img/netflix/{date}'
    print(f'{IMG_DIR}')
    for key in container:
        tTitle = key
        tFile = f'{IMG_DIR}/{tTitle}.png'
        print(f'{tFile}')
        reTitle = regex.change_hyphen(tTitle)

        tweet_format = f'[{reTitle}]\n 공개 여정일:{container[key]}'
        api.update_with_media(tFile, status=tweet_format)
