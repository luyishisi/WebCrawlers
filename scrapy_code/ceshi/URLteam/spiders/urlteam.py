#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from URLteam.items import UrlteamItem


class URLteamSpider(Spider):
    name = "urlteam"
    #减慢爬取速度 为1s
    download_delay = 1
    allowed_domains = ["urlteam.org"]
    start_urls = [
        #"http://xxgege.net/xscs/"
        "http://xxgege.net/xscs/kunansuiyueyiSXS2013/"
    ]

    def parse(self, response):
        sel = Selector(response)

        #items = []
        #获得文章url和标题
        item = UrlteamItem()

        #article_url = str(response.url)

        #article_url = sel.xpath('//a[contains(@class, "name")]/@href').extract()
        
        article_name = sel.xpath('//div[contains(@class ,"con")]/p').extract()
        #print article_name
        #print len(article_url)
        #for i in range(len(article_url)):
        item['article_name'] = article_name[0].encode('utf-8')
        #    item['article_url'] = article_url[i].encode('utf-8')
            #item['article_name'] = [i.encode('utf-8') for i in article_name]
        #item['article_url'] = ['http://xxgege.net'+n.encode('utf-8') for n in article_url]#.encode('utf-8')
        print item 
        return item
'''
        yield item

        #获得下一篇文章的url
        urls = sel.xpath('//div[@class="nav-previous"]/a/@href').extract()

        for url in urls:
            print url
            yield Request(url, callback=self.parse)

'''

