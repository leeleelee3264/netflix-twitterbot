# 셀레니움을 이용해서 다이나믹으로 웹을 조작해서 크롤링을 한다
import time

import driver

TARGET_URL_MUSICAL = "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pCate=&pType=M&pDate="


# def click():

셀레니움으로 페이지 이동 했다가 다시 오고 그러면 이미 새로 랜더링이 되어서
예전의 엘리먼트가 없다고 에러가 났는데 이렇게 해결을 할 수 있었다.
그냥 페이지는 새로 고쳐버리고 몇번째까지 읽었나를 기억하면 그만이었네.. 
https://stackoverflow.com/questions/58717379/how-to-do-loop-with-click-in-selenium
def crawl():
    _driver = driver.get_driver()
    _driver.get(TARGET_URL_MUSICAL)


    find_length = len(_driver.find_elements_by_class_name('prdImg'))
    list_count = 0

    while(list_count < find_length):

        find = _driver.find_elements_by_class_name('prdImg')

        find[list_count].click()

        time.sleep(3)
        _driver.back()
        list_count = list_count + 1


crawl()
