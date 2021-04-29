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


TARGET_URL_MUSICAL = "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pCate=&pType=M&pDate="
TARGET_URL_ACTING = "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01009&pCate=&pType=D&pDate="

DIR_NAME = 'musical'


def crawl():

    today = util._get_date(datetime.datetime.now())
    IMG_DIR = util._get_img_dir(__file__, DIR_NAME)
    TARGET_DIR = f'{IMG_DIR}/{today}'

    isGenerate = util._create_folder(TARGET_DIR)

    if isGenerate is False:
        return

    target_url = [TARGET_URL_MUSICAL, TARGET_URL_ACTING]

    selector = '.rankBody'
    container = []
    img_counter = 0

    for t_url in target_url:
        # crawl from web
        _req = requests.get(t_url)
        _req.encoding = None
        html = _req.content
        _soup = BeautifulSoup(html, 'html.parser')

        infos = _soup.select(selector)

        for info in infos:
            # parsing
            title = info.select_one('.prdInfo')['title']

            _place = info.select_one('.prdInfo > a').contents[2]
            _place2 = _place.replace('\r\n\t', '')
            place = _place2.strip()

            _date = info.select_one('.prdDuration').text
            date = _date.strip()

            container.append(f'타이틀: {title}\n극장: {place}\n일시: {date}')
            print(f'타이틀: {title}\n극장: {place}\n일시: {date}')

            img = info.select_one('.prds > a > img')['src']
            dload.save(img, f'{TARGET_DIR}/{img_counter}.png')

            img_counter = img_counter + 1


crawl()
