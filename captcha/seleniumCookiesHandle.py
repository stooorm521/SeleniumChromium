#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
driver = webdriver.PhantomJS()
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

# delete Cookies
# By name
driver.delete_cookie("CookieName")

# all
driver.delete_all_cookies()