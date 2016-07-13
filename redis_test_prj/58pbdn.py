# -*- coding: utf-8 -*-
__author__ = 'qcl'

from bs4 import BeautifulSoup
import requests

ListOfUrl = []
def GetUrl(url):
    web_info = requests.get(url).text
    soup = BeautifulSoup(web_info, 'html5lib')
    listofa = soup.select('#infolist > table > tbody > tr')
    for i in listofa:
        for j in i.find_all('td'):
            if j['class'] == ['tc']:
                if j.get_text() == '':
                    for k in i.find_all('td'):
                        if k['class'] == ['t']:
                            ListOfUrl.append(k.a['href'])

def GetAllInfo(start, end):
    for i in xrange(start, end + 1):
        url = url = 'http://bj.58.com/pbdn/0/pn' + str(i)
        GetUrl(url)
    for i in ListOfUrl:
        wb_info = requests.get(i).text
        soup = BeautifulSoup(wb_info, 'lxml')
        # titles = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1 ')
        title = soup.title.text
        # time = soup.select('#index_show > ul.mtit_con_left.fl > li.time')
        time = soup.select('.time')
        price = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li > div.su_con > span')
        quality = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')
        area = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span > a')
        print title, time[0].get_text(), price[0].get_text(), quality[0].get_text().strip()
        if len(area) == 2:
            print area[0].get_text() + '-' + area[1].get_text()
        elif len(area) == 1:
            print area[0].get_text()
        print '----------------------------------------------------------------------------'
    print 'done', len(ListOfUrl)


GetAllInfo(1, 20)

