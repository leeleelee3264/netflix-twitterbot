# file for crawl netflix info site
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import os
import dload
import datetime

import regex
import imageTweetTest


def create_folder(fullPath):
    print('working1')
    try:
        if not os.path.exists(fullPath):
            os.makedirs(fullPath)
            return True
        else:
            return False

    except OSError:
        print('ERROR: Creating dir.' + fullPath)
        return False


def crawl():
    print('working2')
    _current_dir = os.path.dirname(os.path.abspath(__file__))
    _path = Path(_current_dir)

    BASE_DIR = _path.parent.absolute()
    IMG_DIR = f'{BASE_DIR}/img/netflix'

    DATE_FORMAT = '%Y%m%d'
    today = datetime.datetime.now()
    fToday = today.strftime(DATE_FORMAT)

    TARGET_DIR = f'{IMG_DIR}/{fToday}'


    # generate folder
    isGenerated = create_folder(TARGET_DIR)

    if isGenerated is False:
        pass
    else:
        TARGET_URL = 'https://movie.daum.net/premovie/netflix?flag=Y'
        TARGET_SELECTOR = '.item_poster'

        _req = requests.get(TARGET_URL)
        _req.encoding = None
        html = _req.content
        _soup = BeautifulSoup(html, 'html.parser')

        # 정보 크롤링
        infos = _soup.select(TARGET_SELECTOR)


        container = {}


        for info in infos:
            title = info.select_one('.thumb_cont > .tit_item > a').text
            date = info.select_one('.thumb_cont > .txt_info > .txt_num').text
            container[title] = date

            _check_img = info.select_one('.thumb_item > .poster_movie > img')

            if _check_img is None:
                del container[title]
                continue

            title_remove_white = regex.change_whitespace(title)
            title_remove_spical = regex.change_file_disable(title_remove_white)

            img = info.select_one('.thumb_item > .poster_movie > img')['src']
            dload.save(img, f'{TARGET_DIR}/{title_remove_spical}.png')

#         # post tweet
#         try:
#             imageTweetTest.post_tweet(container, fToday)
#         except Exception as e:
#             print(e)

print('working')
crawl()
