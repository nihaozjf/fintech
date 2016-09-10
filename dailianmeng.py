#-*-coding:utf-8 -*-
#__autor__='jufu'

import  requests
import urllib2
from bs4 import BeautifulSoup
import pymongo
client =pymongo.MongoClient('localhost',27017)
db = client['fintech']
dailianmengTable=db['dailianmeng']

domainUrl='http://www.dailianmeng.com'
URL='http://www.dailianmeng.com/p2pblacklist/index.html'
baseUrl='http://www.dailianmeng.com/p2pblacklist/index.html?ajax=yw0&P2pBlacklist_page='

def getTotalPages(url):
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	link=soup.select('#yw1 > li.last > a')
	hrefStr= link[0]['href']
	return hrefStr.split('=')[-1]
def genPageUrls(totalPages):
	urls=[baseUrl+str(i) for i in range(1,int(totalPages)+1)]
	return urls
def getPageDetail(urls):
	for url in urls:
		getUserUrls(url)

def getUserUrls(url):
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	users =soup.select('#yw0 > table > tbody > tr')
	for user in users:
		tds=user.findAll('td')
		userName= tds[0].text
		userLink= domainUrl+tds[-1].a['href']
		print userName,userLink
		data={
			'user':userName,
			'url':userLink
		}
		dailianmengTable.insert_one(data)


if __name__=='__main__':
	toatalPages=getTotalPages(URL)
	urls=genPageUrls(toatalPages)
	#print urls[0]
	getPageDetail(urls)