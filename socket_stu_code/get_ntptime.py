#coding:utf-8
#本代码从网洛服务器ntp上获取时间,需要安装sudo apt-get install ntplib*
import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print ctime(response.tx_time)
    
if __name__ == '__main__':
    print_time()
