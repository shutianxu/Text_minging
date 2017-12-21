# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:43:23 2017

@author: 1707500
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS
import jieba.analyse
from snownlp import SnowNLP



# Read the whole text.
text = open('D:\document\crawling\shengdapingjia1.txt', 'r',encoding='utf-8').read()
text = " ".join(jieba.cut(text, cut_all=False))



print(jieba.analyse.extract_tags(text, topK=40, withWeight=True, allowPOS=()))


#a = jieba.analyse.extract_tags(text, topK=40, withWeight=True, allowPOS=('adj'))
#print(a)    


s = SnowNLP(text)
#print(s.words)
print(s.sentiments)
print(s.summary(5))
