import os
from selenium import webdriver as wb

_window = 'nt'
_linux = 'posix'

_dirver_path='C:\\src\\selenium\\chromedriver.exe'
_dirver_path_linux='/home/dev/chromedriver'


def get_driver(headless=True):
    
    real_path=_dirver_path 

    if os.name == _linux:
        real_path=_dirver_path_linux


    if headless is not True:
        return wb.Chrome(executable_path=real_path)

    options = headless_option()
    return wb.Chrome(executable_path=real_path, chrome_options=options)


def headless_option():

    options = wb.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument('disable-gpu')

# 클릭 오류 나서 이걸로 바꿔보려고 함
    options.add_argument("--window-size=1920,1080");
    options.add_argument("--start-maximized");
    options.add_argument("--headless");

    return options


