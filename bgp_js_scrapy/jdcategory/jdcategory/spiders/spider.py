import scrapy
from jdcategory.items import JdcategoryItem
from scrapy.selector import Selector 
from scrapy.http import XmlResponse, HtmlResponse

class Spider(scrapy.Spider):
    name = "jdcategory"
    allowed_domains = ["bgp.he.net"]
    start_urls = [
#   "http://bgp.he.net",
#   "http://bgp.he.net/AS120",
"http://www.httpuseragent.org",
#   "http://bgp.he.net/AS121",
#   "http://bgp.he.net/AS122",
   # "http://www.urlteam.org",
   # "https://www.urlteam.org/wp-admin/admin.php?page=slimview1"
]
    
    def parse(self, response):
        urls = response.css("#allsort a::attr(href)").extract()
        #print 'urls:',response.body
        print '*'*69
        print 'response_type',type(response)
        print 'response_type',str(response)
        print 'response_type',response(str(response))
        
        for url in urls:
            yield scrapy.Request(url,callback = self.parse2)
    
    def parse2(self,response):
        try:
            if isinstance(response,(XmlResponse,HtmlResponse)):
                page = Selector(response)
            else :
                page = Selector(text=response.body)
            categoryPaths = page.css('.breadcrumb a::text').extract()
        except Exception,ex :
            print ex
        if not categoryPaths:
            return None
        item = JdcategoryItem()
        item['categoryPath'] = categoryPaths
        return item

