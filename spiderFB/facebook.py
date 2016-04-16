 #coding:utf-8
 #!/usr/bin/python 
   
import urllib 
import urllib2 
 
from bs4 import BeautifulSoup
from cookielib import CookieJar
import re
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

hosturl = "https://www.facebook.com/"
loginUrl = "https://www.facebook.com/login.php?login_attempt=1&lwv=110"
# req = urllib2.Request(hosturl)
soup = BeautifulSoup('<input class="boldest" Extremely bold >').input
print soup.name
  
logResult =  urllib2.urlopen(hosturl,timeout=1000).read() 
soup = BeautifulSoup(logResult)
#print soup.select("#login_form input")
logInfo = {
	"email": "wanghao5271@hotmail.com",
	"pass":"wanghao@"
}
for i in  soup.select("#login_form input"):
	print i
	tag =BeautifulSoup(str(i)).input
	if tag.get("name") and tag.get("value"):
		logInfo[tag['name']] =  tag.get("value")
		print tag['name'] + "\t" + str(tag.get("value"))


postData = urllib.urlencode(logInfo)
print postData

headers = {
			"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
			"Host": "202.203.222.202",
			"content-type":"application/x-www-form-urlencoded",
			"referer":"https://www.facebook.com/?stype=lo&jlou=AfeSfaeiFvsh5xaSSLIuKbHS0F-1AdSjGCnU5GOP8CBizaJ4XrXli8EJH3r_Ws4vPMeDAHJhu_D63lhaUKVQke3GIbC-kcxT1244kgOo7mcROw&smuh=41755&lh=Ac_3mzPw-4ESY0H_",
			"Upgrade-Insecure-Requests": 1
	      } 

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

request = urllib2.Request(loginUrl, postData, headers)
logResult =  opener.open("https://www.facebook.com/").read() 

f=file("G:\\face.html","a+")
f.write(logResult)

'''

def getHTML(stdNum):
	cookie = cookielib.CookieJar()
	handler=urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)

	response = opener.open(hosturl)
	for item in cookie:
		if item.name == "JSESSIONID":
			jsessionId = item.value

	loginHTML = response.read()
	searchString = 'name="lt" value='
	try:
		index = loginHTML.index(searchString)
	except Exception as err:
		print "err:\t" + err
		return False
	lt = loginHTML[index +17:index +56]
	# print "lt:\t" + lt
	#print "JD:   "+jsessionId
	targetPost = 'http://202.203.222.202/cas/login;jsessionid='+ jsessionId + '?service=http%3A%2F%2F202.203.222.202%2Fmyspace%2Freader%2Findex'
	headers = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1', 
			"Host": "202.203.222.202",
			"Origin": "http://202.203.222.202",
			"Referer": "http://202.203.222.202/cas/login?service=http://202.203.222.202/myspace/reader/index",
			"Upgrade-Insecure-Requests": 1,
	      } '''
 
