from spider.job_search_project.abstract.impl import lagou

a = lagou.LagouJobSearch()
for i in  range (1,5):
    a.pn = i
    a.search_jobs()
