import json
from urllib import parse

from spider.job_search_project.abstract import abstract_job_search, http_search, abstract_company_search, \
    selenium_search  # import的是module，使用类要加module名.类名
from spider.job_search_project.entity.entity import JobInfo


class LagouJobSearch(abstract_job_search.AbstractJobSearch, http_search.HttpSearch):

    def __init__(self, job_position="大数据开发", city="深圳", pn=1):
        # init方法-构造器，类似scala的this方法，还有个作用是定义属性，如果不定义，无法直接使用父类的属性，
        super().__init__(job_position, city, pn)

    def get_request_cookie_url(self):
        return "https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=" % (
            parse.quote(self.job_position), parse.quote(self.city))  # url编码

    def get_data(self):
        return {
            'first': 'true',
            'pn': str(self.pn),
            'kd': self.job_position
        }

    def get_requet_url(self):
        return "https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false" % (self.city)

    def get_headers(self):
        return {  # referer要进行url编码
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=' % (
                parse.quote(self.job_position), parse.quote(self.city)),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def search_jobs(self):
        json_jobs = self.job_info_parser(self.search())
        print(json_jobs)
        jobs = []
        for json_job in json_jobs:
            job = JobInfo()
            # 封装job实体信息
            job.position_id = json_job["positionId"]
            job.position_name = json_job["positionName"]
            job.company_id = json_job["companyId"]
            job.company_full_name = json_job["companyFullName"]
            job.company_short_name = json_job["companyShortName"]
            jobs.append(job)
        return jobs

    def job_info_parser(self, response):
        json_response = json.loads(response)
        return json_response["content"]["positionResult"]["result"]


class LagouCompanySearch(abstract_company_search.AbstractCompanySearch, selenium_search.Seleniumsearch):

    def __init__(self):
        super().__init__()

    def get_requesst_url(self):
        return "https://www.lagou.com/gongsi/%s.html" % (self._var.company_id)

    def search_company(self):
        self.company_info_parser(self.search())
        self.search()

    def company_info_parser(self, response):  # return company desc
        try:
            self.driver.find_element_by_xpath("//*[@class='text_over']").click()
        except BaseException:
            pass
        spanDesc = self.driver.find_element_by_xpath("//*[@class='company_content']").text
        print(spanDesc)
        pDescs = self.driver.find_elements_by_xpath("//*[@class='company_content']/p")
        for pDesc in pDescs:
            print(pDesc.text)

    def set_var(self, var):
        self._var = var

    def getWaitLoadedXPATH(self):
        return "//*[@class='company_content']"
