#coding:utf-8
from scrapy_redis.spiders import RedisSpider
#from pbdnof58.items import Pbdnof58Loader
from scrapy import log
from pbdnof58.items import UrlteamItem
from scrapy.selector import Selector
from redis import Redis

class Myspider(RedisSpider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'myspider_58'
    #设定redis的key，你可以在redis客户端用llen myspider:start_urls 来查看队列
    redis_key = 'myspider:start_urls'
    download_delay = 0.5
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(Myspider, self).__init__(*args, **kwargs)

    def parse(self, response):

        if(response.status == 403):
            print " 检测到403 错误，正在将本次url重新加入到队列"
            r = Redis()
            r.lpush('myspider:start_urls', response.url)
            print "程序休眠十秒，请尽快处理"
            time.sleep(10)


        print '*'*50+'@@@@@@@@'
        sel = Selector(response)

        item = UrlteamItem()

        try: #店名字
            shop_name = sel.xpath('//h1/text()').extract()
        except:
            shop_name = 'none'

        try: #省名/香港
            province = sel.xpath('//ul[contains(@class,"list-group")]/li/a/text()').extract()[0]
        except:
            province = 'none'

        try:#区名/西贡区
            district = sel.xpath('//ul[contains(@class,"list-group")]/li/a/text()').extract()[1]
        except:
            district = 'none'

        try:#类别（餐饮）
            classify = sel.xpath('//ul[contains(@class,"list-group")]/li/a/text()').extract()[2]
            leibie = [u'商户',u'丽人',u'生活服务',u'商务大厦',u'汽车服务',u'地产小区',u'汽车服务',u'购物',u'餐饮',u'宾馆',u'休闲娱乐',u'金融',u'旅游景点',u'交通设施',u'教育',u'医疗',u'公司企业',u'政府机构',u'其他']
            if(classify  not in leibie):
                classify = 'none'
        except:
            classify = 'none'

        try:#地址
            address = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[2]
        except:
            address = 'none'

        try:#地址
            tell = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[3]
        except:
            tell = 'none'

        try:#大地坐标
            geodetic_coordinates = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[7]
        except:
            geodetic_coordinates = 'none'

        try:#火星坐标
            Mars_coordinates = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[8]
        except:
            Mars_coordinates = 'none'

        try:#火星坐标
            Baidu_coordinates = sel.xpath('//ul[contains(@class,"list-group")]/li/text()').extract()[9]
        except:
            Baidu_coordinates = 'none'

        item['province'] = province
        item['district'] = district
        item['shop_name'] = shop_name
        item['classify'] = classify
        item['geodetic_coordinates'] = geodetic_coordinates
        item['Mars_coordinates'] = Mars_coordinates
        item['address'] = address
        item['tell'] = tell
        item['Baidu_coordinates'] = Baidu_coordinates
        item['url'] = response.url

        print '*'*50+'@@@@@@@@'
        print item

        return item
