# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from sched import scheduler

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class Pbdnof58Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    quality = scrapy.Field()
    area = scrapy.Field()
    UrlofPage = scrapy.Field()

class Pbdnof58Loader(ItemLoader):
    default_item_class = Pbdnof58Item
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
