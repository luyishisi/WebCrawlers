#coding:utf-8
from scrapy_redis.spiders import RedisSpider
from pbdnof58.items import Pbdnof58Loader
from redis import Redis
from scrapy import log
from time import sleep

from scrapy.selector import Selector
from scrapy.spider import Spider

class Myspider(Spider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'myspider_58page'

    #redis_key = 'myspider:58_urls'
    start_urls = [
        "http://www.poi86.com/poi/district/2913/1.html",
        "http://www.poi86.com/poi/district/2914/1.html",
        "http://www.poi86.com/poi/district/2919/1.html",
        "http://www.poi86.com/poi/district/2920/1.html",
        "http://www.poi86.com/poi/district/2921/1.html",
        "http://www.poi86.com/poi/district/2922/1.html",
        "http://www.poi86.com/poi/district/2923/1.html",
        "http://www.poi86.com/poi/district/2924/1.html",
        "http://www.poi86.com/poi/district/2925/1.html",
        "http://www.poi86.com/poi/district/2926/1.html",
        "http://www.poi86.com/poi/district/2927/1.html",
        "http://www.poi86.com/poi/district/2928/1.html",
        "http://www.poi86.com/poi/district/2929/1.html",
        "http://www.poi86.com/poi/district/2930/1.html",
        "http://www.poi86.com/poi/district/2931/1.html",
        "http://www.poi86.com/poi/district/2932/1.html",
        "http://www.poi86.com/poi/district/2933/1.html",
        "http://www.poi86.com/poi/district/2934/1.html"
    ]
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
        page_num_max = sel.xpath('//li[contains(@class,"disabled")]/a/text()').extract()
        temp_num = page_num_max[1].split('/')[1]

        #获取该区的区号
        url = response.url
        temp_quhao = url.split('/')[5]
        print temp_quhao
        #开启redis，拼接下一个url，放入队列
        r = Redis()
        for i in range(int(temp_num)):
            #r.lpush('myspider:58_urls', "http://www.poi86.com/poi/district/2913/1.html")
            url_end =  "http://www.poi86.com/poi/district/"+str(temp_quhao)+"/"+str(i+1) + '.html'
            print url_end
            r.lpush('myspider:58_urls', url_end)

        return None
