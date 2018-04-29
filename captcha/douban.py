#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 导入webdriver API对象，可以调用浏览器和操作页面
from selenium import webdriver
# 导入Keys，可以使用操作键盘、标签、鼠标
# 这里的from是灰色的原因是还没有用到
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
