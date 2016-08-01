#coding:utf-8
from scrapy_redis.spiders import RedisSpider
from pbdnof58.items import Pbdnof58Loader
from redis import Redis
from time import sleep
from scrapy.selector import Selector
from scrapy.spider import Spider

class Myspider(RedisSpider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = '58main_page'
    redis_key = 'myspider:58_urls'
    #start_urls = [
    #'http://www.poi86.com/poi/province/2912.html'
    #"http://www.poi86.com/poi/district/2913/13.html"
    #]
    #这里是抓取每个页码的
    download_delay = 2
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(Myspider, self).__init__(*args, **kwargs)
        self.url = 'http://www.poi86.com'

    def parse(self, response):
        sel = Selector(response)
        #抓取该页面总计多少个分页

        r = Redis()
        temp_page = sel.xpath('//tr/td/a/@href').extract()
        for i in temp_page:
            if(i[5]!='c'):
                url_end =  "http://www.poi86.com"+ i
                print  url_end
                r.lpush('myspider:start_urls', url_end)

        return None
