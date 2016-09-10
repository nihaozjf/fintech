# -*- coding:utf-8 -*-
#__autor__='jufu'

import  requests
import urllib2
from bs4 import BeautifulSoup
import pymongo
client =pymongo.MongoClient('localhost',27017)
db = client['fintech']
#ppdaiTable=db['ppdai2008']

#http://www.ppdai.com/blacklist/2015_m0_p1
baseUrl='http://www.ppdai.com/blacklist/'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def gettotalPages(startUrl):
	req=urllib2.Request(url=startUrl,headers=headers)
	html=urllib2.urlopen(req).read().decode('utf-8')

	#print html
	soup=BeautifulSoup(html,'lxml')
	#link= soup.select('div.fen_ye_nav > div > table > tr > td:nth-of-type(7)> a')[0]
	link= soup.find('div',class_='fen_ye_nav')
	elementTable=link.table
	page=0
	if elementTable!=None:
		elementTr=elementTable.tr
		child= elementTr.findAll('td')[-2]
		hrefStr= child.a['href']
		page= hrefStr.split('/')[2].split('_')[2][1:].strip()
	else:
		page='1'
	return page
	#return hrefStr.split('/')[2].split('_')[2][1:].strip()

def genPageUrl(totalPages,year):
	print 'totalPages is:\t'+totalPages
	pageUrls = [baseUrl+str(year)+'_m0_p'+str(i) for i in range(1,int(totalPages)+1)]
	#print pageUrls
	return pageUrls

def getPageDetail(pageUrls):
	for url in pageUrls:
		print url
		getUsersUrl(url)

def getUsersUrl(pageUrl):
	req=urllib2.Request(url=pageUrl,headers=headers)
	html=urllib2.urlopen(req).read().decode('utf-8')
	soup = BeautifulSoup(html,'lxml')
	links= soup.select('#content_nav > div.next_tab_content > div.black_list_centnav > table  > tr > td:nth-of-type(1) '
	                 '> a')
	for link in links:
		user=link.text
		userUrl= 'http://www.ppdai.com/blacklistdetail/'+user
		data={'user':user,
		      'url':userUrl
		      }
		print data
		ppdaiTable.insert_one(data)


if __name__=='__main__':
	print 'please open http://www.ppdai.com/blacklist'
	year = raw_input('please enter year you want to crawl:')
	if year.isdigit():
		startUrl = baseUrl+str(year)+'_m0_p1'
		#print startUrl
		tableName='ppdai'+str(year)
		ppdaiTable=db[tableName]

		totalPages=gettotalPages(startUrl)
		pageUrls=genPageUrl(totalPages,year)
		getPageDetail(pageUrls)
	else:
		print 'please enter the correct year,it must be digit example:2015'
		exit(0)