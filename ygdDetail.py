#-*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib2
import  time
import pymongo
client =pymongo.MongoClient('localhost',27017)
db = client['fintech']
ygdaiTable=db['ygdai']
ygdaiDetailTable=db['ygdai_detail']


def getUserDetail(userInfo):
	print userInfo['user'],userInfo['url']

	userName=userInfo['user']
	data={u'姓名':userName}

	url=userInfo['url']
	html =requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	info= soup.select('#div-content > div > div.mt20 > div.w500.fl.ml20')
	money=soup.select('div.mt5')
	pres= info[0].findAll('pre')
	list=[]
	if pres !=None:
		for pre in pres:
			value=pre.text.strip()
			list.append(value)
		#print list
		data[u'信息']=list
	if money != None:
		trs= money[0].table.findAll('tr')
		tds0=trs[0].findAll('td',class_='f14')
		list0=[]
		list1=[]
		for td in tds0:
			list0.append(td.text)
		tds1=trs[1].findAll('td',class_='f30 pt5')
		for td in tds1:
			list1.append(td.text)

		for x,y in zip(list0,list1):
			data[x]=y

	data[u'抓取时间']=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	#print data
	ygdaiDetailTable.insert_one(data)
	print 25*'*'

if __name__=='__main__':

	for userInfo in ygdaiTable.find():
		getUserDetail(userInfo)