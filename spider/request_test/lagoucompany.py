import requests
import json, time, random



def gongsi_info(url):  # 定义获取公司信息的函数
    for pn in range(2, 31):
        params = {
            'first': 'false',
            'pn': str(pn),
            'sortField': '0',
            'havemark': '0'
        }  # post请求参数

        try:
                urls = 'https://www.lagou.com/gongsi/'
                s = requests.Session()
                s.get(urls, headers=headers, timeout=3)  # 请求首页获取cookies
                cookie = s.cookies  # 为此次获取的cookies
                response = s.post(url, data=params, headers=headers, cookies=cookie, timeout=5)  # 获取此次文本
                time.sleep(10)
                response.encoding = response.apparent_encoding
                json_data = json.loads(response.text)
                print(json_data)
        except requests.exceptions.ConnectionError:
            pass


if __name__ == '__main__':
    url = 'https://www.lagou.com/gongsi/0-0-0-0.json'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/gongsi/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    gongsi_info(url)
print('finished!!')
