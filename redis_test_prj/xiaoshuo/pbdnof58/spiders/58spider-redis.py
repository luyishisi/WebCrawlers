#coding:utf-8
from scrapy_redis.spiders import RedisSpider
from pbdnof58.items import Pbdnof58Loader
# from scrapy import log


class Myspider(RedisSpider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'myspider_58'
    #设定redis的key，你可以在redis客户端用llen myspider:start_urls 来查看队列长度
    redis_key = 'myspider:start_urls'
    download_delay = 3
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(Myspider, self).__init__(*args, **kwargs)


    def parse(self, response):
        #如果你运行不出结果就在这里重写xpath，
        el = Pbdnof58Loader(response=response)
        
        try:
            name = response.xpath('//span[contains(@class,"fl")]').extract()[0][17:-7:]
            print name
            el.add_value('title',name)

            quality = response.xpath('//div[contains(@class , "con")]').extract()
            el.add_value('quality', quality)
            #quality = quality[1].xpath('div[contains(@class, "su_con")]/span/text()').extract()[0].strip()
            #el.add_xpath('title', '//div[contains(@class , "document")].extract() )
        except:
            print "************error**************"
            pass
        return el.load_item()





