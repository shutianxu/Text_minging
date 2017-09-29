
# coding: utf-8

# In[1]:

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS


# In[2]:

# Read the whole text.
text = open('D:\sanguoyanyi.txt', 'r').read()
text = "/".join(jieba.cut(text, cut_all=False))


# In[3]:

print text


# In[4]:

# 绘图模板，就是最后图片的形状
# alice_mask = np.array(Image.open('D:\qwer.jpg'))


# In[5]:

# 中文需要设置字体,songti.ttf代表宋体
# wc = WordCloud(font_path='D:\simhei.TTF', background_color="white", mask=alice_mask,max_words=50)
wc = WordCloud(font_path='D:\simhei.TTF', background_color="white",width=2000, height=860, margin=2)


# In[6]:


# generate word cloud
wc.generate(text)
 # store to file
wc.to_file('result.png') 
#调节大小


# In[7]:

# show
plt.imshow(wc)
plt.axis("off")

# plt.figure()
# plt.imshow(alice_mask, cmap=plt.cm.gray)
# plt.axis("off")

plt.show()


# In[ ]:



