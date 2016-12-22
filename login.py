#!/usr/bin/env python
#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.phantomjs.service import Service as PhantomJSService
from selenium.webdriver.phantomjs.service import Service as IEDriverServer
import time
import re

url = "http://www.enanchu.com/login"
service_args = [
    '--proxy=10.191.131.48:3128',
    '--proxy-auth=F3220575:weiqian123!',
    ]
# browser = webdriver.PhantomJS(executable_path=r'D:\TestProject\browser-driver\phantomjs.exe',service_args=service_args)
browser = webdriver.Ie(executable_path=r'D:\TestProject\browser-driver\IEDriverServer')

browser.get(url)

username = browser.find_element_by_id('userName')
password = browser.find_element_by_id('password')
login_code = browser.find_element_by_id('login_code')
loginSub = browser.find_element_by_id('loginSub')
username.send_keys('kaifeng')
time.sleep(1)
password.send_keys('123456')
time.sleep(1)
code = raw_input('請輸入驗證碼：')
login_code.send_keys(code)
time.sleep(1)
loginSub.click()
print browser.page_source.encode('utf-8')
