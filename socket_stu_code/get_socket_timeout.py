#coding:utf-8
#本代码用于创建一个套接字对象,查看其默认的超时时间,并且自定义一个超时时间
import socket

def socket_timeout():
    #建立一个套接字对象,第一个参数是地址族,第二个是套接字类型:wq
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "默认的套接字超时时间是: %s" %s.gettimeout()
    s.settimeout(100)
    print "新的套接字超时时间是: %s" %s.gettimeout()

if __name__ == '__main__':
    socket_timeout()
