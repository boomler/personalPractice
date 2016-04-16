
import cookielib
import urllib2
import urllib 
import mechanize
class Acc:
    jar = cookielib.CookieJar()
    cookie = urllib2.HTTPCookieProcessor(jar)       
    opener = urllib2.build_opener(cookie)

    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14",
        "Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "Accept-Language" : "en-us,en;q=0.5",
        "Accept-Charset" : "ISO-8859-1",
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "m.facebook.com"
    }

    def login(self):

        try:
            params = urllib.urlencode({'email':'wanghao5271@hotmail.com','pass':'wanghao@','login':'Log+In'})
            req = urllib2.Request('http://m.facebook.com/login.php?m=m&refsrc=m.facebook.com%2F', params, self.headers)
            print "being here1"
            res = self.opener.open(req)
            print "being here2"
            html = res.read()
            print html
            #print res.getheader('location').split('/')[3]

        except urllib2.HTTPError, e:
            print e.msg
        except urllib2.URLError, e:
            print e.reason[1]
        return False

    def fetch(self,url):
        req = urllib2.Request(url,None,self.headers)
        res = self.opener.open(req)
        return res.read()

bla = Acc()
bla.login()




var http = new XMLHttpRequest();
var url = "https://www.facebook.com/login.php?login_attempt=1&lwv=110";
var params = "email=wanghao5271@gmail.com&pass=wanghao@";
http.open("POST", url, true);

http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

http.onreadystatechange = function() {//Call a function when the state changes.
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
    }
}
http.send(params);