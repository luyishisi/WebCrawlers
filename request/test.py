#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
#爬取网页，获得所有图片链接的列表
def get_imgs(page):
    html=requests.get(page,headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    imgs=soup.select('a.js-entry-detail-link > img')
    img_links=[img.get('src') for img in imgs]
    return img_links
#下载图片
def download(img_link):
    html=requests.get(img_link,headers=headers)
    img=img_link.split('/')[-2]
    with open('img'+'.jpg','wb') as f:
        f.write(html.content)
    print "download "+img+'...'
def main():
    page='http://weheartit.com/inspirations/taylorswift?              scrolling=true&page=1&before=256538431'
    img_links=get_imgs(page)
    for link in img_links:
        download(link)
main()
#download('http://data.whicdn.com/images/208856283/superthumb.jpg') #想直接访问图片链接，结果引发同样错误
