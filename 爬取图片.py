#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
auther: dingshihan
time  ：2019/3/30
"""
import requests
import urllib.request
import time
from lxml import etree
import re
import urllib.parse
import os

def wenjian(way,urlss):
    i = 1
    try:
        for url in urlss:
            urllib.request.urlretrieve(url,way+str(i)+'.jpg')
            i = i + 1
    except urllib.error.HTTPError:
        pass



def urlget(urls, headers):
    urlss = []
    urls = 'https://image.baidu.com/search/acjson'
    data = input('请输入爬取图片类型 \n')
    data = urllib.parse.unquote(data)
    page = 30
    for i in range(10):
        params = {
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': data,  # queryWord=%E5%8F%AF%E7%88%B1%E5%A4%B4%E5%83%8F
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '0',
            'ic': '0',
            'hd': '0',
            'latest': '0',
            'copyright': '0',
            'word': data,  # word=%E5%8F%AF%E7%88%B1%E5%A4%B4%E5%83%8F
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'force': '',
            'cg': 'head',
            'pn': page,
            'rn': '30',
            'gsm': '78',
            '1554200768361': ''
        }
        page = page + 30
        message = requests.get(urls, headers=headers, params=params)
        ress = re.findall('"middleURL":"(.*?)",', message.content.decode('utf-8'), re.S)
        for res in ress:
            print(res)
            urlss.append(res)
    return urlss


if __name__ == '__main__' :
    way = 'D:\py之路长且艰\写的程序\爬虫\图片\ '
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 73.0.3683.86Safari / 537.36'
    }


    urls = {
        'https://image.baidu.com/search/acjson'
    }

    urlss = urlget(urls, headers)
    wenjian(way,urlss)