#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 模拟登陆

from selenium import webdriver
import time

import requests
from PIL import Image
from lxml import etree

if __name__ == '__main__':

    from pyvirtualdisplay import Display

    display = Display(visible=0, size=(800, 800))
    display.start()
    driver = webdriver.Chrome()
    driver.get("http://accounts.douban.com")
    # 输入账号密码
    driver.find_element_by_name("form_email").send_keys("850063314@qq.com")
    driver.find_element_by_name("form_password").send_keys("2w2w2w2w")

    # try一下验证码
    try:
        element = driver.find_element_by_id('captcha_image')
        cheakcode_url = element.get_attribute('src').encode('ascii', 'ignore')
        # 这里返回的是unicode字符串，我们要转成python string 字符串，用encode进行重新编码
        if len(cheakcode_url) != 0:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.103 Safari/537.36',
                'Connection': 'keep-alive'}
            s = requests.session()
            response2 = s.get(url=cheakcode_url, headers=headers)
            # 在当前文件夹保存为code.jpg，注意要用'b'的二进制写的方式，用content来获得bytes格式
            with open('code.jpg', 'wb') as fp:
                fp.write(response2.content)
            # 打开并显示图片
            img = Image.open('code.jpg')
            img.show()
            a = input('输入验证码：')
            time.sleep(15)
            driver.find_element_by_name("capycha-solution").send_keys(a)
            fp.close()
    except:
        pass

    # 模拟点击登录
    driver.find_element_by_xpath("//input[@class='btn-submit']").click()

    # 等待3秒, 防止html没有加载完全
    time.sleep(3)

    # 生成登陆后快照
    driver.save_screenshot("douban333.png")

    with open("douban.html", "w") as file:
        file.write(driver.page_source.encode('utf-8'))

    # 这里用 with open 之前总是报错，还是推荐with open的，自带close()
    # f = open("douban1.html", "w")
    # f.write(driver.page_source.encode('utf-8'))
    # f.close()

    driver.quit()
