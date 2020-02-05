import requests
import time
import json
from urllib import parse
from urllib import request


def main():
    job = 'Java'
    city = '广州'
    url_start = "https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=" % (parse.quote(job),parse.quote(city))
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false" % (city)
    headers = {#referer要进行url编码
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=' % (parse.quote(job),parse.quote(city)),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    for x in range(1, 5):
        data = {
            'first': 'true',
            'pn': str(x),
            'kd': job
                }
        s = requests.Session()
        print(url_start)
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
            print(i["positionName"])
            positionName = i["positionName"]
            print(i["salary"])
            salary = i["salary"]
            print(i["companySize"])
            companySize = i["companySize"]
            print(i["skillLables"])
            skillLables = i["skillLables"]
            print(i["createTime"])
            createTime = i["createTime"]
            print(i["district"])
            district = i["district"]
            print(i["stationname"])
            stationname = i["stationname"]

if __name__ == '__main__':
	main()
