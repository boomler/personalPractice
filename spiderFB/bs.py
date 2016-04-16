import cookielib
import mechanize

# Browser
br = mechanize.Browser()

# Enable cookie support for urllib2
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar(cookiejar)

# Broser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')]  
# authenticate
br.open('https://www.facebook.com/messages/')
br.select_form(nr=0)
 
br.form['email'] = 'wanghao5271@gmail.com'
br.form['pass'] = 'wanghao@'
br.form['persistent'] = '1'
res = br.submit()

print "Success!\n"

url = 'https://www.facebook.com/messages/'
# write the html into file.  to see if I can get my personal Page....
htmlFile = br.open(url).read()
f=file("G:\\face.html","a+")
f.write(htmlFile)