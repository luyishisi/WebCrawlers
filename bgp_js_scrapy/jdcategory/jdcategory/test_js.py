import sys 
import gtk 
import webkit
import jswebkit

def get(url):
    webview = webkit.WebView()
    webview.connect( 'load-finished', lambda v,f: gtk.main_quit() )
    webview.load_uri(url)
    gtk.main()
    js = jswebkit.JSContext( webview.get_main_frame().get_global_context() )
    renderedBody = str( js.EvaluateScript( 'document.body.innerHTML' ) ) 
    print renderedBody
    with open("temp", "wb") as f:
        f.write(renderedBody)                                                                                                         

if __name__ == "__main__":
    #url = sys.argv[1]
    url = "http://bgp.he.net/AS120"
    get(url)
