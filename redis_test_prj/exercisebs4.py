# -*- coding: utf-8 -*-
__author__ = 'qcl'

# 采用的是小猪短租的杭州4月14到4月16日的信息。取用了300个数据，如果你采用的不足300个，注意要去掉重复的。目前发现了一个问题是有人将
# 同样的房源发了多次，目前并没有做这部分的校验工作。


from bs4 import BeautifulSoup
import requests

ListOfUrls = []
page = 1
LenOfUrls = 0
while len(ListOfUrls) != 300:
    url = 'http://hz.xiaozhu.com/search-duanzufang-p'+ str(page) + '-0/?startDate=2016-04-15&endDate=2016-04-16'
    print url
    duanzu = requests.get(url)
    soup = BeautifulSoup(duanzu.text, 'html5lib')
    urls = soup.select('#page_list > ul > li > a')
    try:
        for url1 in urls:
            ListOfUrls.append(url1['href'])
            if len(ListOfUrls) == 300:
                break
    except:
        print url1, page
    finally:
        page += 1
for i in ListOfUrls:
    data = requests.get(i)
    soup = BeautifulSoup(data.text, 'lxml')
    title = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
    price = soup.select('#pricePart > div.day_l > span')
    PhotoOfHome = soup.select('#detailImageBox > div.pho_show_r > div > ul > li:nth-of-type(1) > img')
    NameOfHoster = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sex = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    PhotoOfHoster = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    print '网址 : %s' % (i.encode('utf-8'))
    print '标题 : %s' % (title[0].get_text().encode('utf-8'))
    print '地址 : %s' % (address[0].get_text().encode('utf-8'))
    print '价钱 : %s' % (price[0].get_text().encode('utf-8'))
    print '房间照片 : %s' % (PhotoOfHome[0]['data-bigimg'].encode('utf-8'))
    print '房东名字 : %s' % (NameOfHoster[0].get_text().encode('utf-8'))
    print '房东照片 : %s' % (PhotoOfHoster[0]['src'].encode('utf-8'))
    if sex[0]['class'] == ['member_ico']:
        sex = '男'
    else:
        sex = '女'
    print ('房东性别 : %s') % (sex)
    print '_______________________________________________________________________________________________'

