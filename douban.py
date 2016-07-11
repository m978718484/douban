#!/usr/bin/env python
#coding: utf-8
from __future__ import division
from selenium import webdriver
from selenium.webdriver.phantomjs.service import Service as PhantomJSService
from gevent import monkey
from BeautifulSoup import BeautifulSoup
from progressbar import *
monkey.patch_all()
import gevent
import sys
import time


def doJob(urls,name):
	service_args = [
	    
	    ]
	browser = webdriver.PhantomJS(executable_path=r'D:\TestProject\phantomjs\bin\phantomjs.exe',service_args=service_args)
	wr = open('done/'+name+'.txt','w')
	i = 1
	totalCount = len(urls)
	pb = progressbar(totalCount, "*",name)
	for url in urls:
		browser.get(url)
		pb.progress(i)
		time.sleep(0.5)
		i+=1
		soup = BeautifulSoup(browser.page_source.encode('utf-8'))
		findNames = soup.findAll('div',attrs={'class':'name'})
		if findNames is None:
			print url
		for sub in findNames:
			n = sub.a.string.encode('utf8') if sub.a.string is not None else ''
			pl = sub.span.string.encode('utf8') if sub.span.string is not None else ''
			wr.write(n+','+pl)
			wr.write('\n')
	wr.close()
	browser.quit()
files = {'culture':[],'travel':[],'ent':[],'fashion':[],'life':[],'tech':[]}
for key_fn in files:
	with open(key_fn + '.link','r') as f:
		files[key_fn] = f.read().split('\n')


gevent.joinall([
		gevent.spawn(doJob,files['culture'],'culture'),
		gevent.spawn(doJob,files['travel'],'travel'),
		gevent.spawn(doJob,files['ent'],'ent'),
		gevent.spawn(doJob,files['fashion'],'fashion'),
		gevent.spawn(doJob,files['life'],'life'),
		gevent.spawn(doJob,files['tech'],'tech'),
])
