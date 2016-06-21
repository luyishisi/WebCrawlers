import json
import codecs

class CsdnblogPipeline(object):

    def __init__(self):
        self.file = codecs.open('CSDNBlog_data.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))

        return item

