#coding:utf-8
from scrapy_redis.spiders import RedisSpider
from pbdnof58.items import Pbdnof58Loader
from redis import Redis
from scrapy import log
from time import sleep

class Myspider(RedisSpider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'myspider_58page'
    redis_key = 'myspider:58_urls'
    #这里是抓取每个页码的
    download_delay = 1
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(Myspider, self).__init__(*args, **kwargs)
        self.url = 'http://xxgege.net'

    def parse(self, response):
        el = Pbdnof58Loader(response=response)
        try:
            PageUrl = response.xpath('//a[contains(@class, "next")]/@href').extract()
            self.log(PageUrl, level=log.DEBUG)
        except:
            print "没有读取到下一个，检测是否到最后一页"

        r = Redis()
         
        try:
            try:
                print str('!!!!myspider:58_urls '+self.url+str(PageUrl[0]))
                r.lpush('myspider:58_urls', self.url+PageUrl[0])
                sleep(1)            
            except:
                print "压入新url出错"
                print PageUrl[0]
                pass

            #把新的页面加入待爬去队列
            sleep(1)
            urls = response.xpath('//a[contains(@class , "img_wrap fl")]/@href').extract()
            self.log(len(urls), level=log.DEBUG)

            l = len(urls)
            for i in range(l):
                url = urls[i]
                url = "http://xxgege.net"+url
                #把抓取到的商品url压入队列
                r.lpush('myspider:start_urls', url)
                
        except:
            print "执行爬虫出错"
            pass 
        return el.load_item()
