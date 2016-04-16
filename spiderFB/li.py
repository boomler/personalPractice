import urllib, urllib2, cookielib, webbrowser
email = 'psykher@gmail.com'
password = 'password'
jar = cookielib.CookieJar()
cookie = urllib2.HTTPCookieProcessor(jar)
opener = urllib2.build_opener(cookie)
headers = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
 "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
 "Accept-Language" : "zh-CN,zh;q=0.8",
 "Accept-Charset" : "ISO-8859-1",
 "Content-type": "application/x- CodeGo.net ",
 "Host": "m.facebook.com"
}
url = ' CodeGo.net '
data = urllib.urlencode({'email':email,'pass':password,'login':'Entrar'})
req = urllib2.Request(url , data , headers)
'''
$.post("")
res = opener.open(req)
html = res.read()
file = open('login.html', 'a')
file.write(html)
file.close()
text = 'UP! :)'
url = ' CodeGo.net '
data = urllib.urlencode({'comment_text':text,'post':'Comentar'})
req = urllib2.Request(url , data , headers)
res = opener.open(req)
html = res.read()
file = open('post.html', 'a')
file.write(html)
file.close()
raw_input()'''
