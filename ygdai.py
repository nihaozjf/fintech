#-*- coding:utf-8 -*-
# __autor__='jufu'

import requests
from bs4 import BeautifulSoup
import  pymongo
client =pymongo.MongoClient('localhost',27017)
db = client['fintech']
ygdaiTable=db['ygdai']

URL='http://www.ygdai.com/s/blacklist.html'
domain='http://www.ygdai.com'
baseUrl='http://www.ygdai.com/s/blacklist/page/'

def getTotalPages(url):
	html=requests.get(url)
	content =html.text
	soup=BeautifulSoup(content,'lxml')
	link=soup.select('#yw0 > li.last > a')
	hrefStr= link[0]['href']
	return hrefStr.split('/')[-1].split('.')[0]
def genPageUrls(totalPages):
	urls=[baseUrl+str(i)+'.html' for i in range(1,int(totalPages)+1)]
	return urls
def getPageDetail(urls):
	for url in urls:
		print url
		getUsersUrl(url)
def getUsersUrl(url):
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	#print soup.prettify()
	uis=soup.select('#div-content > div > ul.f12.pt10.pb10.border-dash-b')
	for ui in uis:
		lis=ui.findAll('li')
		extractContent(lis[2])
		'''
		print lis[0]
		print '***************'
		print lis[1]
		print '***************'
		print lis[2]
		print '----------------'
		'''
def extractContent(li):
	#print li

	divs=li.findAll('div')
	a=li.a
	userUrl=domain+a['href']
	userName=a['title'].split('_')[0]
	#print userName, userUrl
	data={
		'user':userName,
		'url':userUrl
	}

	#print data
	ygdaiTable.insert_one(data)


if __name__=='__main__':
	totalPages=getTotalPages(URL)
	urls=genPageUrls(totalPages)
	getPageDetail(urls)
