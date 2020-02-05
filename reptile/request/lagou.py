import json
import time
from urllib import parse

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
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
        time.sleep(5)#必须
        response.encoding = response.apparent_encoding
        text = json.loads(response.text)
        info = text["content"]["positionResult"]["result"]
        for i in info:
            print("=" * 40)
            print(i["companyFullName"])
            companyFullName = i["companyFullName"]
            print(i["companyId"])
            companyId = i["companyId"]
            companyUrl = "https://www.lagou.com/gongsi/%s.html" % (companyId)
            driver.get(companyUrl)
            # 等待页面加载完成
            time.sleep(5) #必须
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@class='company_content']"))
            )
            try:
                driver.find_element_by_xpath("//*[@class='text_over']").click()
            except BaseException:
                pass
            spanText = driver.find_element_by_xpath("//*[@class='company_content']").text
            print(spanText)
            pTexts = driver.find_elements_by_xpath("//*[@class='company_content']/p")
            for pText in pTexts:
                print(pText.text)
            print("=" * 40)


if __name__ == '__main__':
    job = 'Java'
    city = '广州'
    startPage = 1
    endPage = 3
    main(job, city, startPage, endPage)
