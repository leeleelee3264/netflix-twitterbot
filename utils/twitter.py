import os

import tweepy


class TwitterSender:

    def __init__(self):
        self._api_key = 'TWITTER_API_KEY'
        self._api_secret = 'TWITTER_API_SECRET'
        self._access_token = 'TWITTER_ACCESS_TOKEN'
        self._access_token_secret = 'TWITTER_ACCESS_TOKEN_SECRET'

        self._oauth = self._get_oauth()

    def _get_oauth(self):

        api_key = os.environ.get(self._api_key)
        api_key_secret = os.environ.get(self._api_secret)

        access_token = os.environ.get(self._access_token)
        access_token_secret = os.environ.get(self._access_token_secret)

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        return auth

    def send(self, status: str, image: str):
        api = tweepy.API(self._oauth)

        # TODO: 이미지 다운로드 안하고 잘 될까..?
        api.update_with_media(image, status=status)
