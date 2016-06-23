from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from doubanImage.items import DoubanimageItem
import urllib
class DouBanImage(BaseSpider):
  name = "douban"
  allowed_domains = ["douban.com"]
  start_urls = [];
  f = open('douban.txt', 'w')
  for i in range(0,1560,40):
    start_urls.append('http://movie.douban.com/subject/10581289/photos?type=S&start=%d&sortby=vote&size=a&subtype=a'%i)

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//ul/li/div/a/img/@src').extract()
    items = []
    self.f = open('douban.txt', 'a')
    counter=0
    for site in sites:
      
      site = site.replace('thumb','raw')
      self.f.write(site)
      self.f.write('\r\n')
      item = DoubanimageItem()
      item['ImageAddress'] = site
      items.append(item)
      urllib.urlretrieve(site,str(counter)+'.jpg')
      print'--------------------------------------------------------------'
      print '*****************picture '+str(counter)+"  is already downloaded************"
      counter=counter+1;
    self.f.close()
    return items
