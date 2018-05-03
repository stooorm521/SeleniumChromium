#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from PIL import Image
from lxml import etree
import time
# 豆瓣的验证码
if __name__ == '__main__':
    url = 'http://www.douban.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.103 Safari/537.36', 'Connection':'keep-alive'}
    # 定义一个session()的对象实体s来储存cookie
    s = requests.session()
    response1 = s.get(url=url, headers=headers)
    response1.encoding = 'utf-8'
    html1 = response1.text
    selector=etree.HTML(html1)
    #如果验证码存在:
    cheakcode_url = selector.xpath('//img[@id="captcha_image"]/@src')
    data = {}
    if len(cheakcode_url) != 0:
        response2 = s.get(url=cheakcode_url, headers=headers)
        # 在当前文件夹保存为code.jpg，注意要用'b'的二进制写的方式，用content来获得bytes格式
        with open('code.jpg','wb') as fp:
            fp.write(response2.content)
        # 打开并显示图片
        img=Image.open('code.jpg')
        img.show()
        time.sleep(5)
        data['checkCode'] = input('输入验证码：')
        fp.close()
    # 需要给服务端传送的数据，字典格式
    # douban 表单不止这几项，已经废弃
    data['username'] = '850063314@qq.com'
    data['password'] = '2w2w2w2w'
    response3 = s.post(url=url, data=data, headers=headers)
    time.sleep(3)
    print(response3.text)