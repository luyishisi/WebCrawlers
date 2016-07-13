import json
import codecs
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy import log
class CleanPipeline(object):

    def __init__(self):
        self.has = set()

    def process_item(self, item, spider):
        if item.keys() >= 5:
            if item in self.has:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.has.add(item)
                return item



class MySQLPipeline(object):

    def __init__(self):
        self.file = codecs.open('urlteam_data.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))

        return item

