import requests
from bs4 import BeautifulSoup
import urllib2

from util import initLogger
from util import initDB

logger=initLogger('log.conf','dlmLogger')
table=initDB('fintech','cxhDetail_new')

def getUserDetail(url):
	html=requests.get(url)
	content=html.text
	soup=BeautifulSoup(content,'lxml')
	print soup

if __name__=='__main__':
	url='http://www.chengxinhei.com/search/result/id/2388.html'
	getUserDetail(url)