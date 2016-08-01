#mporting base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import random
# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        user_agent_ip_list = [
            
        ]
        #request.meta['proxy'] = "http://115.223.107.52:81"

        proxy_ip = random.choice(user_agent_ip_list)
        print proxy_ip
        request.meta['proxy'] = proxy_ip

        proxy_user_pass = "2476371236@qq.com:luyi123"

        encoded_user_pass = base64.encodestring(proxy_user_pass)
        #print encoded_user_pass
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

        # Set the location of the proxy
        #proxy_ip = random.choice(self.user_agent_ip_list)
        #request.meta['proxy'] = proxy_ip
        print '+'*8, 'the Current ip address is', proxy_ip, '+'*8

    # ip from http://pachong.org/
