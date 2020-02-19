import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv

url = 'https://www.daum.net'

response = requests.get(url)
response = response.text
data = BeautifulSoup(response, 'html.parser')

result = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol> li> div> div> span')

# result_dict = {}
result_list = []
for i in range(0,len(result),4):
    rank = result[i].text
    keyword = result[i+1].text

    result_dict = {'rank': rank,'ranker': keyword}
    result_list.append(result_dict)
    # result_dict[rank] = keyword 


with open('daum_rank.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ('rank', 'ranker')
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for item in result_list:
        writer.writerow(item)
    

    # csv_writer = csv.writer(csvfile)
    # for item, value in result_dict.items():
    #     csv_writer.writerow([item,value])