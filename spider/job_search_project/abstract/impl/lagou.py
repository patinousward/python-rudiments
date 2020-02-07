from urllib import parse

from spider.job_search_project.abstract import abstract_job_search, http_search  # import的是module，使用类要加module名.类名


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

    def get_requet_job_position_url(self):
        return "https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false" % (self.city)

    def get_headers(self):
        return {  # referer要进行url编码
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=' % (
                parse.quote(self.job_position), parse.quote(self.city)),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def search_jobs(self):
        print(self.search())
