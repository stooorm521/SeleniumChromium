#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.switch_to.window("this is window name")

# 也可以使用 window_handles 方法来获取每个窗口的操作对象
for handle in driver.window_handles:
    driver.switch_to_.window(handle)

# 页面的前进与后退
driver.forward()     # 前进
driver.back()        # 后退