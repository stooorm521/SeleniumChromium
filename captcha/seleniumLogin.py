#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 模拟登陆

from selenium import webdriver
import time

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

    with open("douban.html", "w") as file:
        file.write(driver.page_source.encode('utf-8'))

    # 这里用 with open 之前总是报错，还是推荐with open的，自带close()
    # f = open("douban1.html", "w")
    # f.write(driver.page_source.encode('utf-8'))
    # f.close()
    
    driver.quit()