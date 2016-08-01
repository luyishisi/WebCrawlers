# -*- coding:utf-8 -*-

from scrapy.item import Item, Field

class UrlteamItem(Item):

    article_name = Field()
    article_url = Field()

    province = Field()
    district = Field()
    shop_name = Field()
    classify = Field()
    geodetic_coordinates = Field()
    Mars_coordinates = Field()
    address = Field()
    tell = Field()
