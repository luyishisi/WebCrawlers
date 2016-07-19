import sys
sys.path.append("/data/scrapy_worlspaces/firstcrawler/firstcrawler")
from scrapy.http import Request,FormRequest,HtmlResponse
import gtk
import webkit
import jswebkit
import settings

class WebkitDownloader(object):
    def process_request(self,request,spider):
        print '1111111'
        print spider.name
        if spider.name in settings.WEBKIT_DOWNLOADER:
            print '2222'
            if(type(request) is not FormRequest):
                    
                print '333333'
                webview = webkit.WebView()
                print request.url
                #webview.conner('load-finished',lambda v,f:gtk.main_quit())
                webview.connect('load-finished',lambda v,f:gtk.main_quit())
                webview.load_uri(request.url)
                gtk.main()
                js = jswebkit.JSContext(webview.get_main_frame().get_global_context())
                renderedBody = str( js.EvaluateScript( 'document.body.innerHTML' ) )
                print renderedBody
                return HtmlResponse( request.url, body=renderedBody )

