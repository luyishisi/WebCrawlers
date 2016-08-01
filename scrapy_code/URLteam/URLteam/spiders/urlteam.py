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
        "http://www.poi86.com/poi/8738259.html",
        "http://www.poi86.com/poi/28525990.html",
        "http://www.poi86.com/poi/28525982.html"
    ]

    def parse(self, response):
        sel = Selector(response)
        #print response.body
        #items = []
        #获得文章url和标题
        item = UrlteamItem()

        try: #店名字
            shop_name = sel.xpath('//h1/text()').extract()
        except:
            shop_name = 'none'
        try: #省名/香港
            province = sel.xpath('//ul[contains(@class,"list-group")]/li/a/text()').extract()[0]
        except:
            province = 'none'
        try:#区名/西贡区
            district = sel.xpath('//ul[contains(@class,"list-group")]/li/a/text()').extract()[1]
        except:
            district = 'none'
        try:#类别（餐饮）
            classify = sel.xpath('//ul[contains(@class,"list-group")]/li/a/text()').extract()[2]
        except:
            classify = 'none'
        try:#地址
            address = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[2]
        except:
            classify = 'none'
        try:#大地坐标
            geodetic_coordinates = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[8]
        except:
            geodetic_coordinates = 'none'
        try:#火星坐标
            Mars_coordinates = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[9]
        except:
            Mars_coordinates = 'none'
        try:
            tell = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[3]
        except:
            tell = 'none'

    #    item['longitude_latitude'] = article_name
        #item['ip'] = article_url
        #item['bs'] = 'poi'

        item['province'] = province
        item['district'] = district
        item['shop_name'] = shop_name
        item['classify'] = classify
        item['geodetic_coordinates'] = geodetic_coordinates
        item['Mars_coordinates'] = Mars_coordinates
        item['address'] = address
        item['tell'] = tell

        print '*'*50+'@@@@@@@@'
        print item
        return item
