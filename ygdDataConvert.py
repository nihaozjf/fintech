#-*-coding:utf-8 -*-
#__autor__='jufu'

from util import initLogger
from util import initDB

logger=initLogger('log.conf','dlmLogger')
#logger.info('dlm logger error')

if __name__=='__main__':


	table=initDB('fintech','ygdai_detail')
	newTable=initDB('fintech','new_ygdai_detail')
	for user in table.find():

		data={}
		for userString in user[u'信息']:

			for s in userString.split('\n'):
				#print s.split(u'\uff1a')
				key=s.split(u'\uff1a')[0].strip()
				value=s.split(u'\uff1a')[1].strip()
				#data[str(count)]=key+':'+value
				data[key]=value
				#print key,value

				#print data
				#newTable.insert_one(data)

			
		data[u'抓取时间']=user[u'抓取时间']
		data[u'总逾期借款笔数']=user[u'总逾期借款笔数']
		data[u'逾期最大天数']=user[u'逾期最大天数']
		data[u'总逾期本金']=user[u'总逾期本金']
		print data
		newTable.insert_one(data)
		
