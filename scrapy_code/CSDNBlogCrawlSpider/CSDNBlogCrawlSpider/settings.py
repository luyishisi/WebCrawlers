# -*- coding: utf-8 -*-

# Scrapy settings for CSDNBlogCrawlSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CSDNBlogCrawlSpider'

SPIDER_MODULES = ['CSDNBlogCrawlSpider.spiders']
NEWSPIDER_MODULE = 'CSDNBlogCrawlSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CSDNBlogCrawlSpider (+http://www.yourdomain.com)'

COOKIES_ENABLED = False

ITEM_PIPELINES = {
    'CSDNBlogCrawlSpider.pipelines.CsdnblogcrawlspiderPipeline':301
}
