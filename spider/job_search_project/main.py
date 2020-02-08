from spider.job_search_project.abstract.impl import lagou

job_search = lagou.LagouJobSearch()
company_search = lagou.LagouCompanySearch()
company_full_name_list = []
for i in range(1, 5):
    job_search.pn = i
    jobs = job_search.search_jobs()
    for job in jobs:
        # 写入文件company
        if(company_full_name_list.__contains__(job.company_full_name)):
            print(job.company_full_name  + " 该公司已经搜索过，忽略")
            continue
        company_full_name_list.append(job.company_full_name)
        company_search.set_var(job)
        # 写入文件company
        company = company_search.search_company()
        if (company_search.is_waibao(company.desc)):
            print("-" * 20 + "start" + "-" * 20)
            print("发现外包公司：" + job.company_full_name)
            print(company.desc)
            print("-" * 20 + " end " + "-" * 20)
