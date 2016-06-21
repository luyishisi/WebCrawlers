#!/usr/bin/python
# -*- coding:utf-8 -*-

# from scrapy.contrib.spiders import  CrawlSpider,Rule

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from CSDNBlog.items import CsdnblogItem


class CSDNBlogSpider(Spider):
    """爬虫CSDNBlogSpider"""

    name = "CSDNBlog"

    #减慢爬取速度 为1s
    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [

        #第一篇文章地址
        "http://blog.csdn.net/u012150179/article/details/11749017"
    ]

    def parse(self, response):
        sel = Selector(response)

        #items = []
        #获得文章url和标题
        item = CsdnblogItem()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        item['article_name'] = [n.encode('utf-8') for n in article_name]
        item['article_url'] = article_url.encode('utf-8')

        yield item

        #获得下一篇文章的url
        urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()
        for url in urls:
            print url
            url = "http://blog.csdn.net" + url
            print url
            yield Request(url, callback=self.parse)

