import time

import requests

from spider.job_search_project.abstract.search import Search  # import的是类，不用加module名.类名


class HttpSearch(Search):

    # 获取请求cookie的url，可以是登陆获取（这里子类未实现登陆操作），也可以是未登录状态浏览器打开url后，后台给的临时cookie
    def get_request_cookie_url(self):
        pass

    # 获取请求职位信息的url
    def get_requet_job_position_url(self):
        pass

    # 由解析得到的打开公司网页的方法
    def generate_request_company_url(self):
        pass

    # 获取头信息
    def get_headers(self):
        pass

    def get_data(self):
        pass

    # 核心方法
    def search(self):
        s = requests.session()
        # 不能直接调用get_request_cookie_url 方法
        s.get(self.get_request_cookie_url(), headers=self.get_headers(), timeout=3)
        cookie = s.cookies
        response = s.post(self.get_requet_job_position_url(), self.get_data(), cookies=cookie,
                          headers=self.get_headers(), timeout=3)
        time.sleep(5)
        response.encoding = response.apparent_encoding
        return response.text
