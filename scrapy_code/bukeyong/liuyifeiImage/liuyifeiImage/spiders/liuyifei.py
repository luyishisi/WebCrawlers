from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from liuyifeiImage.items import LiuyifeiimageItem

'''http://movie.douban.com/celebrity/1049732/photos/'''

class liuyifeiImage(BaseSpider):
  name='liuyifei'
  allowed_domain=["douban.com"]
  start_urls=[]
  f=open('liuyifei_pic_address.txt','wb')
  for i in range(0,1120,40):
    start_urls.append('http://movie.douban.com/celebrity/1049732/photos/?type=C&start=%d&sortby=vote&size=a&subtype=a'%i)

  def parse(self,response):
    hxs=HtmlXPathSelector(response)
    sites=hxs.select('//ul/li/div/a/img/@src').extract()
    items=[]
    for site in sites:
      site=site.replace('thumb','raw')
      self.f.write(site)
      self.f.write('\r\n')
      item=LiuyifeiimageItem()
      item['ImageAddress']=site
      items.append(item)
    return items
