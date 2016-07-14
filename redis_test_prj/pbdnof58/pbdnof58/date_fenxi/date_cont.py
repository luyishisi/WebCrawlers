#!/usr/bin/env python
#coding:utf-8
import json

list1 = [0,0,0,0,0,0,0,0,0,0,0]
date = json.load(open('date.json','r'))
sum = 0
for i in range(3200):
    #print date[i]['price'] 
    try:
        num = int(date[i]['price'])
        list1[num/500] += 1
        
    except:
        pass
print "*******"
for i in range(10):
    print str(500*i) + '--' + str(500*(i+1)), list1[i]

print list1
#print sum/1700
#print date
print type(date)

