

from scrapy.item import Item, Field

class CsdnblogcrawlspiderItem(Item):

    blog_name = Field()
    blog_url = Field()

