import os
from time import sleep

import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

from openpyxl import load_workbook

##########################################################################
##################### variable related selenium ##########################
##########################################################################
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('lang=ko_KR')
chromedriver_path = "chromedriver"
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)  # chromedriver 열기

##########################################################################
###################### variable related excel ############################
##########################################################################
rowNum = 1
load_file_name = "outputcafelist.xlsx"
load_wb = load_workbook(os.path.join(os.getcwd(), load_file_name))
load_ws = load_wb['Sheet1']
get_cells = load_ws['A20001':'C27053']

def main():
    global driver, write_wb
    driver.implicitly_wait(4)  # 렌더링 될때까지 기다린다 4초
    driver.get('https://map.kakao.com/')  # 주소 가져오기

    # 카페 정보 읽어오기
    place_infos = []
    for rows in get_cells:
        place = []
        for cell in rows:
            place.append(cell.value)
        place_infos.append(place)
    print('get places')

    for i, place in enumerate(place_infos):
        if i % 5 == 0 and i != 0:
            sleep(5)
        print("#####", i, '/', place[0])
        search(place)

    # chrome 종료
    driver.quit()
    print("finish")

def search(place_infos):
    global driver

    cafe_no = place_infos[0]
    name = place_infos[1]
    addr = place_infos[2]

    search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
    search_area.send_keys(name)  # 검색어 입력
    driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)  # Enter로 검색
    sleep(1)

    # 1번 페이지 cafe list 읽기
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    cafe_lists = soup.select('.placelist > .PlaceItem')

    if crawling(cafe_no, name, addr, cafe_lists):
        search_area.clear()
    else:
        try:
            driver.find_element_by_xpath('//*[@id="info.search.place.more"]').send_keys(Keys.ENTER)
            sleep(1)

            # 2~ 5페이지 읽기
            # 여기도 없으면 없는걸로 간주?
            for i in range(2, 6):
                # 페이지 넘기기
                xPath = '//*[@id="info.search.page.no' + str(i) + '"]'
                driver.find_element_by_xpath(xPath).send_keys(Keys.ENTER)
                sleep(1)

                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                cafe_lists = soup.select('.placelist > .PlaceItem')

                # 일치하는거 찾았으면 종료 아니면 다음 페이지 찾기기
                if crawling(cafe_no, name, addr, cafe_lists):
                    return
        except ElementNotInteractableException:
            print('not found')
        finally:
            search_area.clear()

def crawling(cafe_no, name, addr, cafe_lists):
    """
    :param cafe_no: 카페 index
    :param name: 카페 이름
    :param addr: 카페 주소
    :param cafe_lists: 이름으로 검색된 카페들 목록
    :return: 크롤링 성공 여부(카페를 찾았는가??)
    """

    flag = False
    for i, cafe in enumerate(cafe_lists):
        cafe_name = cafe.select('.head_item > .tit_name > .link_name')[0].text  # cafeName
        cafe_address = cafe.select('.info_item > .addr > p')[0].text  # cafe address

        # 카페 정보가 일치하는 경우에만 상세정보 페이지에서 리뷰 읽기
        if cafe_name == name and cafe_address == addr:
            detail_page_xpath = '//*[@id="info.search.place.list"]/li[' + str(i + 1) + ']/div[5]/div[4]/a[1]'
            try:
                driver.find_element_by_xpath(detail_page_xpath).send_keys(Keys.ENTER)
                driver.switch_to.window(driver.window_handles[-1])  # 상세정보 탭으로 변환
                sleep(1)

                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')   # 상세정보 페이지 읽기

                temp_image = soup.select('.details_present > .link_present > span')
                thumb_image = ''
                #print(temp_image)
                if len(temp_image) > 1:
                    thumb_url = 'http:' + temp_image[0]['style'].split(':')[1][5:-2]
                    #print(thumb_url)
                    urllib.request.urlretrieve(thumb_url, './img/img' + str(cafe_no)+'.jpg')
                else:
                    print('no image')
                driver.close()
                driver.switch_to.window(driver.window_handles[0])  # 검색 탭으로 전환
                return True
            except NoSuchElementException:
                print("not cafe info list")

    return flag

if __name__ == "__main__":
    main()
