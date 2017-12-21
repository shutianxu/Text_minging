# coding:utf-8
import itchat
import re
itchat.login()
friends = itchat.get_friends(update=True)[0:]
tList = []
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)
    # 拼接字符串
    text = "".join(tList)
# jieba分词
import jieba
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)
# wordcloud词云

print(wl_space_split)
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


wc = WordCloud(font_path='D:\simhei.TTF', background_color="white",width=2000, height=860, margin=2)

# generate word cloud
wc.generate(text)
 # store to file
wc.to_file('result.png') 
#调节大小
# show
plt.imshow(wc)
plt.axis("off")

# plt.figure()
# plt.imshow(alice_mask, cmap=plt.cm.gray)
# plt.axis("off")

plt.show()
# =============================================================================
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
# import os 
# import numpy as np
# import PIL.Image as Image
# d= os.path.dirname(os.path.abspath( __file__ ))
# alice_coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))
# my_wordcloud = WordCloud(background_color="white", max_words=2000,mask=alice_coloring,max_font_size=400, random_state=420,font_path='/Users/sebastian/Library/Fonts/Arial Unicode.ttf').generate(wl_space_split)
# image_colors = ImageColorGenerator(alice_coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
# =============================================================================
