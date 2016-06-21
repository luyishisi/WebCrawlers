# -*- coding: utf-8 -*-

# Scrapy settings for CSDNBlog project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CSDNBlog'

SPIDER_MODULES = ['CSDNBlog.spiders']
NEWSPIDER_MODULE = 'CSDNBlog.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CSDNBlog (+http://www.yourdomain.com)'

#禁止cookies,防止被ban  
COOKIES_ENABLED = False  
  
ITEM_PIPELINES = {  
    'CSDNBlog.pipelines.CsdnblogPipeline':300  
}  
