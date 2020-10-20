from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import unicodedata

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
special_character_pattern = re.compile('[^\w\s]')

with open('receiptReview.txt', 'w', -1, 'utf-8') as f:
    for i in range(0,59):
        url = 'https://store.naver.com/restaurants/detail?entry=pll&id=895457986&query=%EC%B9%B4%ED%8E%98%20%EB%85%B8%ED%8B%B0%EB%93%9C%20%EC%B2%AD%EB%8B%B4&tab=receiptReview&tabPage=' + str(i)
        print("now is "+ str(i)+ "page")
        webpage = urlopen(url)
        source = BeautifulSoup(webpage,'html.parser')
        reviews = source.find_all('div', {'class': 'review_txt'})
        scores = source.find_all('span', {'class': 'score'})

        for i, review in enumerate(reviews):
            text = review.get_text().strip().replace('\n', ' ') # \U0001f44d
            text = emoji_pattern.sub(r'', text) # 이모티콘 제거
            text = special_character_pattern.sub(r'', text) # 특수문자 제거
            if text != '':
                f.write(text + '/' + scores[i].get_text() + '\n')
print('finish')