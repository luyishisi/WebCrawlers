#!/usr/bin/python
# -*- coding:utf-8 -*-

# from scrapy.contrib.spiders import  CrawlSpider,Rule

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from URLteam.items import UrlteamItem


class URLteamSpider(Spider):
    name = "urlteam"
    #减慢爬取速度 为1s
    download_delay = 2
    allowed_domains = ["urlteam.org"]
    start_urls = [
        #"http://www.urlteam.org/2016/06/scrapy-%E5%85%A5%E9%97%A8%E9%A1%B9%E7%9B%AE-%E7%88%AC%E8%99%AB%E6%8A%93%E5%8F%96w3c%E7%BD%91%E7%AB%99/"

        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/",
        "http://icanhazip.com/"

    ]

    def parse(self, response):
        sel = Selector(response)

        #items = []
        #获得文章url和标题
        item = UrlteamItem()

        article_url = str(response.url)
        #article_name = sel.xpath('//h1/text()').extract()
        article_name = sel.xpath('/html/body/div[1]').extract()
        print article_name
        item['article_name'] = [n.encode('utf-8') for n in article_name]
        item['article_url'] = article_url.encode('utf-8')
        yield item


        #获得下一篇文章的url
        #urls = sel.xpath('//div[@class="nav-previous"]/a/@href').extract()
        #urls = 'http://www.j4.com.tw/james/remoip.php'
        #yield Request(urls, callback=self.parse)
        '''
        for url in urls:
        #    print url
        #    print "!!!!!!!!!!!!kankan yield yunxingbu "
            yield Request(url, callback=self.parse)
        #    print "kankan yield yunxingbu "
        '''
