import os
from selenium import webdriver as wb

_window = 'nt'
_linux = 'posix'

_dirver_path='C:\\src\\selenium\\'


def get_driver():
    if(os.name == _linux):
        # 나중에 리눅스 구현
        pass

    full_path = f'{_dirver_path}chromedriver.exe'

    print(full_path)
    return wb.Chrome(executable_path=full_path)


