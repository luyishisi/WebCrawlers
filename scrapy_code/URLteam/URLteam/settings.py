# -*- coding: utf-8 -*-

# Scrapy settings for urlteam project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'URLteam'

SPIDER_MODULES = ['URLteam.spiders']
NEWSPIDER_MODULE = 'URLteam.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'urlteam (+http://www.yourdomain.com)'
#禁止cookies,防止被ban
COOKIES_ENABLED = False

ITEM_PIPELINES = {
    'URLteam.pipelines.UrlteamPipeline':300
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'URLteam.middlewares.ProxyMiddleware': 100,
}
