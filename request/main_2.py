#coding:utf-8
#完成通用爬虫，抓取一个页面队列中所有图片

import requests
import re
import time
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
def download(url):
    try:
        r = requests.get(url,headers=headers,timeout = 50)
        name = int(time.time())
        f = open('./pic/'+str(name)+'.jpg','wb')
        f.write(r.content)
        f.close()
    except:
        pass

def list_img_url(url):
    try:
        r = requests.get(url, timeout = 50 , headers=headers)
        img_list = re.findall("http://pic.meizitu.com/wp-content/uploads/.*jpg",r.text)
        print img_list
        for i in img_list:
            print i
            download(i)
    except:
        pass

def get_big_img_url():
    for i in range(100):
        try:
            num = 5300+i;
            url ='http://www.meizitu.com/a/'+ str(num) +'.html'
            img_url = requests.get(url)
            img_url_list = re.findall('http://pic.meizitu.com/wp-content/uploads/2016a/.*.jpg',img_url.text)
            for url in img_url_list:
                l = len(re.findall('limg',url))
                #print "l: ",l
                if(l == 0):
                    print "url: ",url
                    download(url)
                    time.sleep(1)
        except:
            print "qing求发送失败重试"
            time.sleep(10)
            continue



if __name__ == '__main__':
    url = 'http://www.meizitu.com/a/list_1_'
    print "begin"
    get_big_img_url()
    #for i in range(1,10):
    #    try:
    #        temp_url =  url + str(i) + '.html'
    #        print temp_url
    #        list_img_url(temp_url)
    #        time.sleep(1)
    #    except:
    #        pass

    #list_url()
    #download()
