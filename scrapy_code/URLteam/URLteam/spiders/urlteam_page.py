#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from URLteam.items import UrlteamItem
from scrapy_redis.spiders import RedisSpider
import re
import os
import time

#class URLteamSpider(RedisSpider):
class URLteamSpider(Spider):
    name = "poi_page"
    #减慢爬取速度 为1s
    download_delay = 3
    allowed_domains = ["www.poi86.com"]

    '''start_urls = [
        "http://www.poi86.com/poi/8738259.html",
        "http://www.poi86.com/poi/28525990.html",
        "http://www.poi86.com/poi/28525982.html"
    ]'''
    redis_key='poi'
    #print start_url
    def parse(self, response):
        print '*'*50+'@@@@@@@@'
        sel = Selector(response)

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

        item['longitude_latitude'] = article_name
        item['ip'] = article_url
        item['bs'] = 'poi'

        item['province'] = province
        item['district'] = district
        item['shop_name'] = shop_name
        item['classify'] = classify
        item['geodetic_coordinates'] = geodetic_coordinates
        item['Mars_coordinates'] = Mars_coordinates
        item['address'] = address

        print '*'*50+'@@@@@@@@'
        print item
        return item
