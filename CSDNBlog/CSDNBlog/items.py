# -*- coding:utf-8 -*-

from scrapy.item import Item, Field

class CsdnblogItem(Item):

    article_name = Field()
    article_url = Field()
