import requests
from bs4 import BeautifulSoup
import urllib2

import pymongo
client =pymongo.MongoClient('localhost',27017)
db = client['fintech']
chengxinheiTable=db['chengxinhei']

def getUserDetail(url):
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	print soup

if __name__=='__main__':
	url='http://www.chengxinhei.com/search/result/id/2388.html'
	getUserDetail(url)