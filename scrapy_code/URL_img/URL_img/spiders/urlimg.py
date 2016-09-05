# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from URL_img.items import UrlImgItem

class UrlimgSpider(scrapy.Spider):
    name = "urlimg"
    allowed_domains = ["https://www.urlteam.org"]
    start_urls = (
        #'https://www.urlteam.org/',
        'https://www.urlteam.org/2016/08/%E7%88%AC%E8%99%AB%E7%A0%B4%E8%A7%A3ip%E9%99%90%E5%88%B6-adsl%E5%8A%A8%E6%80%81ip%E6%9C%8D%E5%8A%A1%E5%99%A8-%E9%83%A8%E7%BD%B2%E5%B0%8F%E7%BB%93/',
    )

    def parse(self, response):
        sel =Selector(response)
        items = UrlImgItem()
        url = sel.xpath('//img/@src').extract()
        print url
        items['image_urls'] = url
        return items
