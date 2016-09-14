# __author__ = 'zhangjufu'
# -*- coding:utf-8 -*-

import logging
import logging.config
import pymongo


def initLogger(confFile,logger):
	logging.config.fileConfig(confFile)
	logger = logging.getLogger(logger)
	return logger

def initDB(db,table,client='localhost',port=27017):
	client =pymongo.MongoClient(client,port)
	db = client[db]
	table=db[table]
	return table
