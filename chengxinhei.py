# -*-coding:utf-8 -*-
# __autor__='jufu'
import requests
from bs4 import BeautifulSoup


from util import initLogger
from util import initDB

logger = initLogger('log.conf', 'dlmLogger')
table = initDB('fintech', 'chengxinhei_new')

baseUrl = 'http://www.chengxinhei.com/search/list/page/'
URL = 'http://www.chengxinhei.com'


def getTotalPages(url):
    html = requests.get(url)
    content = html.text
    soup = BeautifulSoup(content, 'lxml')
    lastNumber = soup.find('li', class_='last')
    hrefStr = lastNumber.a['href']
    return hrefStr.split('/')[4].split('.')[0]


def genPageUrls(totalPages):
    print 'total pages is ' + totalPages
    urls = [baseUrl + str(i) + '.html' for i in range(1, int(totalPages) + 1)]
    return urls


def getPageDetail(urls):
    for url in urls:
        print 'page url is:\t' + url
        getUsersUrl(url)


def getUsersUrl(url):
    html = requests.get(url)
    content = html.text
    soup = BeautifulSoup(content, 'lxml')
    links = soup.findAll('div', class_='w80')
    for link in links:
        userUrl = URL + link.a['href']
        print 'user url is:\t' + userUrl
        data = {'url': userUrl}
        table.insert_one(data)


if __name__ == '__main__':
    url = baseUrl + '1.html'
    totalPages = getTotalPages(url)
    urls = genPageUrls(totalPages)
    getPageDetail(urls)
