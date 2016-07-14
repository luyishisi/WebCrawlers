
import json
import codecs

class UrlteamPipeline(object):

    def __init__(self):
        i = 1
        
    def process_item(self, item, spider):

        self.file = codecs.open('%d.json' %i, mode='wb', encoding='utf-8')
        i += 1
        print i

        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))

        return item


