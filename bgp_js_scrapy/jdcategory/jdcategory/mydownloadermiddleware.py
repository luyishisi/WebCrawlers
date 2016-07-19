import sys
sys.path.append("/data/scrapy_worlspaces/firstcrawler/firstcrawler")
from scrapy.http import Request,FormRequest,HtmlResponse
import gtk
import webkit
import jswtbkit
import settings

class WebkitDownloader(object):
    def process_request(self,request,spider):
        print '1111111'
        if spider.name in settings.WEBKIT_DOWNLOADER:
            print '123123'
            webview = webkit.WebView()
            webview.conner('load-finished',lambda v,f:gtk.main_quit())
            webview.load_url(request.url)
            gtk.main()
            js = jswebkit.JSContext( webview.get_main_frame().get_global_context() )
            renderedBody = str( js.EvaluateScript( 'document.body.innerHTML' ) )
            return HtmlResponse( request.url, body=renderedBody )

