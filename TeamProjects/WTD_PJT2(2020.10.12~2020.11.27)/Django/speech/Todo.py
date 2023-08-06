#!/usr/bin/env python
# coding: utf-8

# In[1]:


from konlpy.tag import Okt
import json
import os
import numpy as np
import pandas as pd
from pprint import pprint
import nltk
from tensorflow import keras

class ToDoList():

    def __init__(self):
        print("초기화 ON")
        root = os.path.dirname(os.path.abspath(__file__))
        print(root)
        path = os.path.join(root, 'ToDoList.h5')
        self.new_model = keras.models.load_model(path)
        self.okt = Okt()
        path2 = os.path.join(root, 'train_docs.json')
        with open(path2 , encoding='UTF8') as f:
            self.train_docs = json.load(f)
        self.tokens = [t for d in self.train_docs for t in d[0]]
        self.text = nltk.Text(self.tokens, name='NMSC')
        self.selected_words = [f[0] for f in self.text.vocab().most_common(1000)]

    def tokenize(self, doc):
        # norm은 정규화, stem은 근어로 표시하기를 나타냄
        return ['/'.join(t) for t in self.okt.pos(doc, norm=True, stem=True)]

    def term_frequency(self, doc):
        return [doc.count(word) for word in self.selected_words]

    def predict2(self, review):
        token = self.tokenize(review)
        tf = self.term_frequency(token)
        data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
        score = float(self.new_model.predict(data))
        if(score > 0.85):
            return 1
        else:
            return 0   
