# file for crawl netflix info site

import requests
from bs4 import BeautifulSoup
import os
import dload
import datetime

from crawl.test import test_print


def createFolder(fullPath):
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
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMG_DIR = f'{BASE_DIR}/img/netflix'

    DATE_FORMAT = '%Y%m%d'
    today = datetime.datetime.now()
    fToday = today.strftime(DATE_FORMAT)

    TARGET_DIR = f'{IMG_DIR}/{fToday}'


    # generate folder
    isGenerated = createFolder(TARGET_DIR)

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

        # test
        test_print()

        for info in infos:
            title = info.select_one('.thumb_cont > .tit_item > a').text
            date = info.select_one('.thumb_cont > .txt_info > .txt_num').text
            container[title] = date

            _check_img = info.select_one('.thumb_item > .poster_movie > img')

            if _check_img is None:
                del container[title]
                continue

            img = info.select_one('.thumb_item > .poster_movie > img')['src']
            dload.save(img, f'{TARGET_DIR}/{title}_{fToday}.png')
