
# coding: utf-8

# In[1]:

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
import jieba.posseg as pseg
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud, STOPWORDS


# In[2]:

# Read the whole text.
text = open('D:\sanguoyanyi.txt', 'r').read()
text = " ".join(jieba.cut(text, cut_all=False))
# result=[]
# result.append(text)


# In[4]:

vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
analyze = vectorizer.build_analyzer()
result = analyze(text)


# In[9]:

a=''
for i in result:
    a = a+' '+i
b=[]
b.append(a)


# In[11]:


transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
tfidf=transformer.fit_transform(vectorizer.fit_transform(b))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重


# In[12]:

for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    print u"-------文本的词语tf-idf权重------"
    for j in range(len(word)):
        print word[j],weight[i][j]


# In[ ]:

# words=pseg.cut(text)
# a=[',','《','》','|','-',':','。','、','“','”','！','1','2','3','4','5','6','7','8','9','0',' ']
# result=[]
# for key in words:
#     if key not in a:
#         result.append(key.word)


# In[ ]:



