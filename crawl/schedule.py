import io
import math
import os
import sys

import requests
from PIL import Image
from tweepy import TweepError

from crawl import imageTweetTest
from crawl.util import download_img_with_url
from db import exe_query

sys.path.append('/opt/twitter_project')


keys = {
    imageTweetTest.API_KEY: "vhBAZqnCy7eoBAkyI2YOZaIDF",
    imageTweetTest.API_KEY_SECRET: "5Ck4kciJVTqat9H7CXbdodJXXSBZhimgpE0uHLQKwISMH912Jk",
    imageTweetTest.ACCESS_TOKEN: "1447910219787292677-k5D6LNoFMR0KljSncmH1JEQwzrpeBZ",
    imageTweetTest.ACCESS_TOKEN_SECRET: "unCorvWn7RSexWDpbBvSY541hInN66RmdoESNabvNlyB0",
}


def crawl():
    list = exe_query.get_schedule_for_twitter()

    for casting in list:
        name = casting.get('name')
        cast = casting.get('cast')
        time = str(casting.get('time'))[:5]
        place = casting.get('place')

        fmt = f'TITLE: {name} \n\n캐스팅:{cast}\n시간:{time}\n공연장:{place}'

        url = casting.get('poster_path')
        file_name = download_img_with_url(url)

        try:
            imageTweetTest.post_tweet_img_di(file_name, fmt, keys)
        except TweepError as e:
            print(str(e))
        finally:
            os.remove(file_name)


if __name__ == "__main__":
    crawl()
