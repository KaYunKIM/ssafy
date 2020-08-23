import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

from openpyxl import load_workbook
from openpyxl import Workbook

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('lang=ko_KR')
chromedriver_path = "resources/chromedriver"
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)  # chromedriver 열기

def main():
    global driver
    places = ['종로구 사직동', '종로구 삼청동']
    driver.implicitly_wait(4)  # 렌더링 될때까지 기다린다 4초
    driver.get('https://map.kakao.com/')  # 주소 가져오기

    # 검색
    for place in places:
        search(place)

    driver.quit()

def search(place):
    global driver
    cafeName = ''
    cafeAddress = ''
    cafeOper = ''

    searchArea = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
    searchArea.send_keys(place + " 카페")  # 검색어 입력
    driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)  # Enter로 검색
    time.sleep(1)

    # 검색된 정보가 있는 경우에만 탐색
    try:
        # 1번 페이지 cafe list 읽기
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        cafeLists = soup.select('.placelist > .PlaceItem')

        for cafe in cafeLists:
            print(cafeLists[0].select('.head_item > .tit_name > .link_name')[0].text)

        # 장소 더 보기 클릭
        # driver.find_element_by_xpath('//*[@id="info.search.place.more"]').send_keys(Keys.ENTER)
        # cafeList = driver.find_elements_by_class_name('PlaceItem clickArea')
        # print(cafeList)
    except NoSuchElementException:
        res = "no more info btn"
    finally:
        searchArea.clear()  # 기존 검색어 지우기

    return res

if __name__ == "__main__":
    main()