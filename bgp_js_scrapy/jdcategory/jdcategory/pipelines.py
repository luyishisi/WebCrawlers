# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals 
import json 

class JdcategoryPipeline(object):
    def __init__(self):
        self.file = open("jdcategory","w")
    
    def process_item(self, item, spider):
        line = ""
        for word in item['categortPaeh']:
            line = line + word.strip()+';'
        if line:
            self.file.write(line[0:-1].encode("utf-8")+'\n')
        else :
            self.file.write(str(item)+'\n')
        return item
    def spider_closed():
        self.file.close()

