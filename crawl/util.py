# Project: twitter_project
# Author: absin
# Date: 2021-04-22
# DESC: Util code for netflix and musical crawl
import os
from pathlib import Path

DATE_FORMAT = '%Y%m%d'


def _create_folder(fullPath):
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


def _get_date(targetDate, fix_format=True):

    return targetDate.strftime(DATE_FORMAT)


def _get_img_dir(file, dirName):

    _current_dir = os.path.dirname(os.path.abspath(file))
    _path = Path(_current_dir)

    base_dir = _path.parent.absolute()

    return f'{base_dir}/img/{dirName}'

