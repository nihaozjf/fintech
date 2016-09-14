#-*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib2
import  time

from util import initLogger
from util import initDB

logger=initLogger('log.conf','dlmLogger')
mongoTable=initDB('fintech','dlmDetail_new')

def getUserDetail(userInfo):
	#print userInfo

	url=userInfo['url']
	userName=userInfo['user']
	#print userName
	logger.info('start to get user detail:\t'+url)

	print 'crawl user:', userName,url
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	table=soup.table
	trs= table.findAll('tr')
	data={u'姓名':userName}
	#print data
	for tr in trs:
		th=tr.th
		td=tr.td
		if td.a!=None:
			#print th.text+":"+td.a['href']
			key=th.text
			value=td.a['href']
			print key,value

		else:
			#print th.text+":"+td.
			key=th.text
			value=td.text
			print key,value
		data[key]=value

	#print data
	data[u'抓取时间']=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	mongoTable.insert_one(data)


if __name__=='__main__':

	dailianmengTable=initDB('fintech','dailianmeng_new')
	for userInfo in dailianmengTable.find():
		getUserDetail(userInfo)