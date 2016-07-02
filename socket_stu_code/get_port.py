#coding:utf-8
#运行此代码可以活取range区间内端口号与其中作用
import socket
def get_port():
    for i in range(1,65000):
        try:
            print "port:%s name:%s" %(i, socket.getservbyport(i))
        except:
            continue
    
if __name__ == '__main__':
    get_port()
