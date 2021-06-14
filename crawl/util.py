# Project: twitter_project
# Author: absin
# Date: 2021-04-22
# DESC: Util code for netflix and musical crawl
import os
from pathlib import Path
#from PIL import Image

DATE_FORMAT = '%Y%m%d'


def _create_folder(fullPath):
    try:
        if not os.path.exists(fullPath):
            os.makedirs(fullPath)
            return True
        else:
            return False

    except OSError:
        print('ERROR: Creating dir.' + fullPath)
        return False


def _get_date(targetDate, fix_format=True):

    return targetDate.strftime(DATE_FORMAT)


def _get_img_dir(file, dirName):

    _current_dir = os.path.dirname(os.path.abspath(file))
    _path = Path(_current_dir)

    base_dir = _path.parent.absolute()

    return f'{base_dir}/img/{dirName}'


#def _resize_img(file, dirName, hig, wid):
#    with Image.open(f'{dirName}/{file}.png') as im:
#        new_img = im.resize((hig, wid), Image.ANTIALIAS)
#        new_img.save(f'{dirName}/{file}.png')
