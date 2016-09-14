#-*-coding:utf-8 -*-
#__autor__='jufu'

import  requests
import urllib2
from bs4 import BeautifulSoup
import pymongo
import logging
import logging.config

domainUrl='http://www.dailianmeng.com'
URL='http://www.dailianmeng.com/p2pblacklist/index.html'
baseUrl='http://www.dailianmeng.com/p2pblacklist/index.html?ajax=yw0&P2pBlacklist_page='

from util import initLogger
from util import initDB

logger=initLogger('log.conf','dlmLogger')
table=initDB('fintech','dailianmeng_new')

def getTotalPages(url):
	logger.info('start to get total url...')
	logger.info(url)
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	link=soup.select('#yw1 > li.last > a')
	hrefStr= link[0]['href']
	logger.info('getTotalPages end...')
	return hrefStr.split('=')[-1]
def genPageUrls(totalPages):
	urls=[baseUrl+str(i) for i in range(1,int(totalPages)+1)]
	return urls
def getPageDetail(urls):
	for url in urls:
		getUserUrls(url)

def getUserUrls(url):
	#print 'get user url....'
	logger.info('start to get user url:\t'+url)
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	users =soup.select('#yw0 > table > tbody > tr')
	#print 'soup select...'
	for user in users:
		tds=user.findAll('td')
		userName= tds[0].text
		userLink= domainUrl+tds[-1].a['href']
		print userName,userLink
		data={
			'user':userName,
			'url':userLink
		}
		print data

		table.insert_one(data)


if __name__=='__main__':
	toatalPages=getTotalPages(URL)
	urls=genPageUrls(toatalPages)
	#print urls[0]
	getPageDetail(urls)