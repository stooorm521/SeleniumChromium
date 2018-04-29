#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 模拟登陆

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import codecs

if __name__ == '__main__':

    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(800, 800))
    display.start()

    driver = webdriver.Chrome()
    driver.get("http://www.douban.com")

    # 输入账号密码
    driver.find_element_by_name("form_email").send_keys("850063314@qq.com")
    driver.find_element_by_name("form_password").send_keys("2w2w2w2w")

    # 模拟点击登录
    driver.find_element_by_xpath("//input[@class='bn-submit']").click()

    # 等待3秒, 防止html没有加载完全
    time.sleep(3)

    # 生成登陆后快照
    driver.save_screenshot("douban.png")

    f=open("douban.html", "w")
        # strin=u''.join((driver.page_source)).encode('utf-8').strip()
    f.write(driver.page_source.encode('utf-8'))
        # p.agent_info = u' '.join((agent_contact, agent_telno)).encode('utf-8').strip()
    driver.quit()