# -*- coding: utf-8 -*-
import urllib
import urllib2
postdata=urllib.urlencode({
    'username':'汪小光',
    'password':'why888',
    'continueURI':'http://www.verycd.com/',
    'fk':'',
    'login_submit':'登录'
})
req = urllib2.Request(
    url = 'http://secure.verycd.com/signin',
    data = postdata
)
result = urllib2.urlopen(req)
print result.read()
