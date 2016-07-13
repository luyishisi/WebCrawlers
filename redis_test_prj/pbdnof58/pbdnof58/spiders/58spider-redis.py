from scrapy_redis.spiders import RedisSpider
from pbdnof58.items import Pbdnof58Loader
# from scrapy import log


class Myspider(RedisSpider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'myspider_58'
    redis_key = 'myspider:start_urls'
    download_delay = 1
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(Myspider, self).__init__(*args, **kwargs)


    def parse(self, response):

        el = Pbdnof58Loader(response=response)
        el.add_xpath('title', '//h1/text()')
        el.add_xpath('price', '//span[contains(@class, "price c_f50")]/text()'.strip())
        quality = response.xpath('//ul[contains(@class, "suUl")]/li')
        quality = quality[1].xpath('div[contains(@class, "su_con")]/span/text()').extract()[0].strip()
#        quality = '9'
        el.add_value('quality', quality)
        area = response.xpath('//span[contains(@class, "c_25d")]/a/text()'.strip())
        if area == []:
            area = 'None'
        elif len(area) == 1:
            area = area[0].extract()
        else:
            area = area[0].extract() + '-' + area[1].extract()
        el.add_value('area', area)
        el.add_xpath('time', '//li[contains(@class, "time")]/text()')
        return el.load_item()





