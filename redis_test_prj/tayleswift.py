# -*- coding: utf-8 -*-
__author__ = 'qcl'

from urllib import urlretrieve
from bs4 import BeautifulSoup
import requests

listofpic = []
def getpiclist(url):
    wb_data = requests.get(url).text
    soup = BeautifulSoup(wb_data, 'html5lib')
    urls = soup.select('#main-container > div > div.grid-thumb.grid-responsive > div > div > div > a > img')
    for url in urls:
        listofpic.append(url['src'])
def getpicture(first, last):
    for i in xrange(first, last + 1):
        url = 'http://weheartit.com/inspirations/taylorswift?page=' + str(i)
        getpiclist(url)
    for i in xrange(len(listofpic)):
        postfix = listofpic[i].split('.')[-1]
        local = 'E:\\tayleswift\\tayleswift' + str(i) + '.' + postfix
        urlretrieve(listofpic[i], local)
    print 'done'
getpicture(1, 20)

