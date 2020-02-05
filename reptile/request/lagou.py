import json
import time
from urllib import parse
from selenium import webdriver,common
import requests


def main(job, city, start=1, end=5):
    url_start = "https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=" % (
        parse.quote(job), parse.quote(city))
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false" % (city)
    headers = {  # referer要进行url编码
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=' % (
            parse.quote(job), parse.quote(city)),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    for x in range(start, end):
        data = {
            'first': 'true',
            'pn': str(x),
            'kd': job
        }
        s = requests.Session()
        s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
        cookie = s.cookies  # 为此次获取的cookies
        response = s.post(url_parse, data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
        time.sleep(5)
        response.encoding = response.apparent_encoding
        text = json.loads(response.text)
        info = text["content"]["positionResult"]["result"]
        for i in info:
            print(i["companyFullName"])
            companyFullName = i["companyFullName"]
            print(i["companyId"])
            companyId = i["companyId"]
            companyUrl = "https://www.lagou.com/gongsi/%s.html" % (companyId)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(companyUrl)
            contents = driver.find_elements_by_xpath("//*[@class='company_content']/p")
            for content in contents:
                print(content.text)



if __name__ == '__main__':
    job = 'Java'
    city = '广州'
    startPage = 1
    endPage = 3
    main(job, city, startPage, endPage)
