from spider.job_search_project.abstract.impl import lagou

job_search = lagou.LagouJobSearch()
company_search = lagou.LagouCompanySearch()
for i in range(1, 5):
    job_search.pn = i
    jobs = job_search.search_jobs()
    for job in jobs:
        company_search.set_var(job)
        company_search.search_company()
