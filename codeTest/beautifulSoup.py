# -*- coding: utf-8 -*-
#http://www.qiushibaike.com/8hr/page/1?s=4603425
import urllib2
from bs4 import BeautifulSoup
import time
if __name__ == '__main__':
    page = 1
    xiubai=open(r'xiubai.txt','w+')
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    for page in range(1, 11):
        # debug了一晚上，这里的request不能单纯的只用url，而要自定义headers，否则会报错
        url = "http://www.qiushibaike.com/8hr/page/"+str(page)
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response.read())
        time.sleep(5)
        for result in soup.findAll("div", "content", title=True):
            xiubai.write(result.get_text())