#-*- coding:utf-8 -*-

import requests
from bs4 import  BeautifulSoup
import sys
import urllib2

baseUrl = 'http://www.p2p12580.com/blacklist.asp?'

def getDetail(url):
	pass
def gettotalPages(startUrl):

	#http://www.p2p12580.com/blacklist.asp?page=1&id=1&strKeyWord=
	#html=requests.get(startUrl)
	html=urllib2.urlopen(startUrl).read().decode('gbk')
	soup=BeautifulSoup(html,'lxml')
	#print soup
	print soup.select('#__01 > tbody > tr:nth-of-type(6) > td:nth-of-type(2) > table > tbody > tr:nth-of-type(39) > td')

if __name__=='__main__':
	print 'please open http://www.p2p12580.com/blacklist.asp'
	id = raw_input('please enter id:')
	if id.isdigit():
		startUrl = baseUrl+'page=1&id='+str(id)+'&strKeyWord='
		print startUrl
		gettotalPages(startUrl)
	else:
		print 'please enter the correct id,it must be digit'
		exit(0)