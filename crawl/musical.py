# Project: twitter_project
# Author: absin
# Date: 2021-04-22
# DESC: file for crawl musical info site

from pathlib import Path

import requests
from bs4 import BeautifulSoup
import os
import util
import dload
import datetime


TARGET_URL = "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pType=D"
DIR_NAME = 'musical'

_current_dir = os.path.dirname(os.path.abspath(__file__))


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

    # image downloading
    _path = Path(_current_dir)
    BASE_DIR = _path.parent.absolute()
    IMG_DIR = f'{BASE_DIR}/img/{DIR_NAME}'

    DATE_FORMAT = '%Y%m%d'

    selector = '.rankBody'

    _req = requests.get(TARGET_URL)
    _req.encoding = None
    html = _req.content
    _soup = BeautifulSoup(html, 'html.parser')

    infos = _soup.select(selector)

    for info in infos:
        print(info)




# calling
# crawl()
print(util._get_img_dir(__file__, DIR_NAME))