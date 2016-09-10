#-*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib2
import  time
import pymongo
client =pymongo.MongoClient('localhost',27017)
db = client['fintech']
dailianmengTable=db['dailianmeng']
dlmDetailTable=db['dlm_detail']

def getUserDetail(userInfo):
	#print userInfo
	url=userInfo['url']
	userName=userInfo['user']
	#print userName
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
	dlmDetailTable.insert_one(data)




if __name__=='__main__':
	#for userInfo in chengxinheiTable.find():
	#	getUserDetail(userInfo)
	#userInfo=dailianmengTable.find_one()
	for userInfo in dailianmengTable.find():
		getUserDetail(userInfo)