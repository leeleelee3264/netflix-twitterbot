# Project: twitter_project
# Author: absin
# Date: 2021-03-25
# DESC:
import re

HYPHEN = '_'
AT = '@'
WHITE_SPACE = ' '

REGEX_HYPHEN = r'[_]'
REGEX_WHITE_SPACE = r'[\s]'
REGEX_FILE_DISABLE = r'[-=+,#/\?:^$.*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]'


# _을 공백으로 바꾸기
def change_hyphen(txt):
    t_text = txt
    results = re.findall(REGEX_HYPHEN, t_text)

    t_text = re.sub(REGEX_HYPHEN, WHITE_SPACE, t_text, len(results))

    return t_text


# 공백을 _로 바꾸기
def change_whitespace(txt):
    t_text = txt
    results = re.findall(REGEX_WHITE_SPACE, t_text)

    t_text = re.sub(REGEX_WHITE_SPACE, HYPHEN, t_text, len(results))

    return t_text


# 파일 이름에 못들어가는 특수 문자 @로 바꾸기
# ? <>
def change_file_disable(file_name):
    t_file_name = file_name
    results = re.findall(REGEX_FILE_DISABLE, file_name)

    t_file_name = re.sub(REGEX_FILE_DISABLE, AT, t_file_name, len(results))

    return t_file_name

