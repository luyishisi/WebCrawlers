# -*- coding: utf-8 -*-

# Scrapy settings for meizitu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'
#载入ImageDownLoadPipeline类
ITEM_PIPELINES = {'meizitu.pipelines.ImageDownloadPipeline': 1}
#图片储存
IMAGES_STORE = '.'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meizitu (+http://www.yourdomain.com)'
