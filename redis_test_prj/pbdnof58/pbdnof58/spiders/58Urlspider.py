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
        self.url = 'http://bj.58.com'

    def parse(self, response):
        el = Pbdnof58Loader(response=response)
        PageUrl = response.xpath('//a[contains(@class, "next")]/@href').extract()
        self.log(PageUrl, level=log.DEBUG)
        r = Redis()
        if PageUrl != []:
            r.lpush('myspider:58_urls', self.url + PageUrl[0])
            #把新的页面加入待爬去队列
            sleep(1)
            el.add_value('UrlofPage', self.url + PageUrl[0])
        #urls = response.xpath('//table[contains(@class, "tbimg")]/tr')
        urls = response.xpath('//td[contains(@class, "t")]/a/@href')
        self.log(len(urls), level=log.DEBUG)
        print "------"
        print urls
        print "------"
        l = len(urls)
        #for url in urls:
        for i in range(l):
            #url = url.xpath('td[contains(@class, "t")]/a/@href').extract()
            url = urls.extract()[i]
            print "**** url ****"
            print url
            print "**** url ****"
            if len(url) <= 201:# and 'zhuan' not in url:
                print "**** yes ****!!!!"
                #把抓取到的商品url压入队列
                r.lpush('myspider:start_urls', url)
        return el.load_item()
