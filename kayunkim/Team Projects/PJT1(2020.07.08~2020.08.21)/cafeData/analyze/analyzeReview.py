import re
import networkx  # pip install networkx
import itertools
import os

from collections import Counter
from konlpy.tag import Okt
from hanspell import spell_checker
from openpyxl import load_workbook

okt = Okt()
KEYWORD_NUM = 4

def xplit(*delimiters):
    return lambda value: re.split('|'.join([re.escape(delimiter) for delimiter in delimiters]), value)

class Sentence:

    @staticmethod
    def co_occurence(sentence1, sentence2):
        p = sum((sentence1.bow & sentence2.bow).values())
        q = sum((sentence1.bow | sentence2.bow).values())
        return p / q if q else 0

    def __init__(self, text, index=0):
        self.index = index
        self.text = text
        self.nouns = okt.nouns(self.text)
        self.bow = Counter(self.nouns)

    def __eq__(self, another):
        return hasattr(another, 'index') and self.index == another.index

    def __hash__(self):
        return self.index



def get_sentences(text):
    candidates = xplit('.', '?', '!', '\n', '.\n')(text.strip())
    sentences = []
    index = 0
    for candidate in candidates:
        candidate = candidate.strip().replace('&', ', ')
        result = spell_checker.check(candidate) # spell check
        candidate = result.checked
        if len(candidate):
            normalized_text = "".join(okt.normalize(candidate))
            sentences.append(Sentence(normalized_text, index))
            index += 1
    return sentences


def build_graph(sentences):
    graph = networkx.Graph()
    graph.add_nodes_from(sentences)
    pairs = list(itertools.combinations(sentences, 2))
    for eins, zwei in pairs:
        graph.add_edge(eins, zwei, weight=Sentence.co_occurence(eins, zwei))
    return graph

def extract_keyword(review):
    global dic
    cafeno = review[0]
    place_name = review[1]
    text = ''
    score = 0
    num = 0

    # 리뷰를 한 줄로 묶기
    for i, content in enumerate(review):
        # 카페번호, 이름은 넘기기
        if i == 0 or i == 1:
            continue
        
        # 텍스트와 별점 분리
        decode_text = content.decode()
        review_text = decode_text[:-2]
        rating = decode_text[-1]

        # 평점 4점 이상의 리뷰만 분석
        if rating.isdigit():
            if float(rating) >= 4:
                text += review_text + '. '
        else:
            print('return')
            return
        num += 1
        score += float(rating)

    #print(score / num)  # 평균 평점
    sentences = get_sentences(text)
    graph = build_graph(sentences)
    pagerank = networkx.pagerank(graph, weight='weight')
    reordered = sorted(pagerank, key=pagerank.get, reverse=True)

    # make stop_word set
    stop_words = set()
    with open('stopwords.txt', 'r', encoding='utf-8-sig') as ff:
        while True:
            linee = ff.readline()
            if not linee: break
            stop_words.add(linee.replace('\n', ''))

    # 카페 이름 stopword에 추가
    place_name_token = okt.nouns(place_name)
    for tok in place_name_token:
        stop_words.add(tok)

    # keyword extraction
    keywords = set()
    for sen in reordered:
        #print(sen.text)
        flag = True
        for noun in sen.nouns:
            if noun not in stop_words:
                keywords.add(noun)

            # 키워드 최대 4개 까지만 뽑기기
            if len(keywords) >= KEYWORD_NUM:
                flag = False
                break
        if flag == False:
            break

    #print(place_name.decode(), keywords)

    # 파일에 저장
    with open('keywords2.txt', 'a', encoding='utf-8') as ff:
        for i, key in enumerate(keywords):
            save_text = str(cafeno) + ',' + str(i+1) + ',' + key + '\n'
            ff.write(save_text)
            if dic.get(key) != None:
                dic[key] += 1
            else:
                dic[key] = 1



load_file_name = "reviewLists_all.xlsx"
load_wb = load_workbook(os.path.join(os.getcwd(), load_file_name))
load_ws = load_wb['Sheet1']
#get_cells = load_ws['A2':'BO2000']
get_cells = load_ws['A2':'BO12487']
dic = {}
reviews = []
for rows in get_cells:
    review = []
    for cell in rows:
        if cell.value != None:
            if type(cell.value) == type('string'):
                review.append(cell.value.encode('utf-8'))
            else:
                review.append(cell.value)
    reviews.append(review)

for i, review in enumerate(reviews):
    if len(review) >= 17:
        extract_keyword(review)
    if i % 10 == 0:
        print(i)

print('finish')
print(dic)
print(len(dic))