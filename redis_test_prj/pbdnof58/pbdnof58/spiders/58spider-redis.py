#coding:utf-8
from scrapy_redis.spiders import RedisSpider
from pbdnof58.items import Pbdnof58Loader
# from scrapy import log


class Myspider(RedisSpider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'myspider_58'
    #设定redis的key，你可以在redis客户端用llen myspider:start_urls 来查看队列
    redis_key = 'myspider:start_urls'
    download_delay = 1
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(Myspider, self).__init__(*args, **kwargs)


    def parse(self, response):
        #如果你运行不出结果就在这里重写xpath，
        el = Pbdnof58Loader(response=response)

        try:
            el.add_xpath('title', '//h1/text()')
            el.add_xpath('price', '//span[contains(@class, "price_now")]/i/text()'.strip())
        except:
            el.add_value('title', 'title_none')
            el.add_value('price', 'price_none')

        try:
            quality = response.xpath('//ul[contains(@class, "suUl")]/li')
            quality = quality[1].xpath('div[contains(@class, "su_con")]/span/text()').extract()[0].strip()
            el.add_value('quality', quality)
        except:
            el.add_value('quality', 'quality')

        try:
            area = response.xpath('//div[contains(@class, "palce_li")]/span/i/text()'.strip())
            if area == []:
                area = 'None'
            elif len(area) == 1:
                area = area[0].extract()
            else:
                area = area[0].extract() + '-' + area[1].extract()
            el.add_value('area', area)
        except:
            el.add_value('area', 'error')

        try:
            el.add_xpath('time', '//li[contains(@class, "time")]/text()')
        except:
            pass
        return el.load_item()





