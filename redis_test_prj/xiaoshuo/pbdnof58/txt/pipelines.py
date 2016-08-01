#coding:utf-8
import json
import codecs
from scrapy import signals
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors

mysql_db={'landmark':"""insert into landmark2(latitude,longitude,address) values('%s','%s','%s')""",
          'Whois':"""insert into whois2(table1,sx,key1) values("%s","%s","%s")""",
          'osm':"""insert into osm(ll,rgb) values("%s","%s")""",
          'justping':"""insert into justping(address,mintime,ip) values("%s","%s","%s")""",
          'ipip':"""insert into ipipping2(address,mintime,ip) values("%s","%s","%s")""",
          'rtb':"""update 005_Syria_ip set flag="%s" where ip="%s" """,
          'rtb_2':"""insert into rtb(ip,longitude_latitude) values('%s','%s')"""
}

class UrlteamPipeline(object):

    def __init__(self):
        self.file = codecs.open('urlteam_data.json', mode='ab', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item

class MySQLStoreCnblogsPipeline(object):

    def __init__(self, dbpool):
        print 'init' ,dbpool
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=int(settings['MYSQL_PORT']),
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d
    #将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
#        print item['bs'] =='landmark'
#        print mysql_db[item['bs']] , item['ip'] , item['longitude_latitude']
        if item['bs'] =='rtb':
            print mysql_db[item['bs']],item['flag'],item['ip'],item['flag']==2
            conn.execute("""
                    %s
            """ % mysql_db[item['bs']] % (item['flag'],item['ip']))
            print '执行update完成！'
            if(item['flag']==2):
                print '执行insert 开始！'
                conn.execute("""
                    %s
                """ % mysql_db['rtb_2'] % (item['ip'], item['longitude_latitude']) )

    def _get_linkmd5id(self, item):
        #url进行md5处理，为避免重复采集设计
        return md5(item['link']).hexdigest()
    #异常处理
    def _handle_error(self, failue, item, spider):
        log.err(failure)

'''
        if item['bs']=='justping':
            print '执行 justping!~!!!!!!!!!!!!'
            for i in range(0,int(item['wz'])):
#                print mysql_db[item['bs']] % (item['address'+str(i)],item['minTime'+str(i)],item['ip'])
                conn.execute("""
                        %s
                        """ % mysql_db[item['bs']] % (item['address'+str(i)],item['minTime'+str(i)],item['ip']))
        if item['bs']=='ipip':
            print '执行 ipip!~~~~~~~~~~~~~'
            for i in range(0,int(item['wz'])):
#                print mysql_db[item['bs']] % (item['address'+str(i)],item['minTime'+str(i)],item['ip'])
                f.write(mysql_db[item['bs']] % (item['address'+str(i)],item['minTime'+str(i)],item['ip']))
                conn.execute("""
                        %s
                        """ % mysql_db[item['bs']] % (item['address'+str(i)],item['minTime'+str(i)],item['ip']))
'''
#        print item['bs']
#        print mysql_db[item['bs']]
#        linkmd5id = self._get_linkmd5id(item)
#        #print linkmd5id
#        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
#        conn.execute("""
#                select 1 from cnblogsinfo where linkmd5id = %s
#        """, (linkmd5id, ))
#        ret = conn.fetchone()
#
#        if ret:
#            conn.execute("""
#                update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
#            """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id))
#            #print """
#            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
#            #""", (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
#        else:
#            conn.execute("""
#                insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
#                values(%s, %s, %s, %s, %s, %s)
#            """, (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now))
#            #print """
#            #    insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
#            #    values(%s, %s, %s, %s, %s, %s)
#            #""", (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now)
    #获取url的md5编码
