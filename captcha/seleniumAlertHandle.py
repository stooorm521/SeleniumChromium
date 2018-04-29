#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 弹窗提示
# 当你触发了某个事件之后，页面出现了弹窗提示，处理这个提示或者获取提示信息方法如下：
from selenium import webdriver
# 导入 ActionChains 类
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS()
alert = driver.switch_to.alert()