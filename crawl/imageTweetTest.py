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

    _current_dir = os.path.dirname(os.path.abspath(__file__))
    _path = Path(_current_dir)

    BASE_DIR = _path.parent.absolute()
    IMG_DIR = f'{BASE_DIR}/img/netflix/alba-icon.png'

    # TODO: 여기다가 이미지 넣는 방법 찾아야 한다
    tweet_format = '이미지 테스트'
    api.update_with_media(IMG_DIR, status=tweet_format)




