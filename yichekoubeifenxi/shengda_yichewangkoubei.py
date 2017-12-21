# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:37:36 2017

@author: 1707500
"""

import requests
from requests.exceptions import RequestException
import re
import json
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
def get_one_page(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code ==200:
            return response.text
        return None
    except RequestException:
        return None
    
def parse_one_page(html):
    pattern = re.compile('href="http://car.bitauto.com/xinshengda/koubei/(\d+)/"',re.S)
    items = re.findall(pattern,html)
    try:    
        patternscore = re.compile('class=total2>(.*?)</',re.S)
        score = re.findall(patternscore,html)
    except:
        pass
#    for item in items:
#        yield{
#               'rank':item[0], 
#               'name':item[1],
#               'year':item[2],
#               'daoyan':item[3],
#               'zhuyan':item[4]+','+item[5],
#               'type':item[6]+','+item[7],
#               'jieshao':item[8],
#               'fenshu':item[9]+item[10]
#                }
    return items
def parse_one_page_zonghe(html):
    pattern = re.compile('class="head".*?class="start".*?style="width:(.*?)%;.*?<p>(.*?)</p>',re.S)
    items = re.findall(pattern,html)
    try:    
        patternscore = re.compile('class=total2>(.*?)</',re.S)
        score = re.findall(patternscore,html)
    except:
        pass    
    for item in range(len(items)):
        if (items[item][1] != items[item-1][1]):
            print(items[item][1])
            write_to_file(items[item][1])
        
def write_to_file(content):
    with open('D:\document\crawling\shengdapingjia1.txt','a',encoding = 'utf-8') as f:
        f.write(content  +'\n')
        f.close()
    
def main():
    a=[]
    for i in range(130):
        url = 'http://car.bitauto.com/xinshengda/koubei/gengduo/3821-0-0-0-0-0-0-0-0-0-0--'+str(i+1)+'-10.html'
        html = get_one_page(url)        
        for j in parse_one_page(html):
            a.append(j)
    for k in a[::2]:
        koubei_url = 'http://car.bitauto.com/xinshengda/koubei/'+str(k)+'/'
        koubei_html = get_one_page(koubei_url)
        parse_one_page_zonghe(koubei_html)
        
if __name__ == '__main__':
    main()
    