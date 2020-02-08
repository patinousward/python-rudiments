import os
import time

from spider.job_search_project.abstract.impl import lagou

web = "lagou"
position_name = "python开发"
city = "北京"
start = 2
end = 5

print("开始搜索,网站：%s 职位名称：%s 城市：%s 开始页数：%s 结束页数：%s" % (web, position_name, city, start, end))
time.sleep(3)
os.remove("./waibao.txt")
os.remove("./non-waibao.txt")
job_search = lagou.LagouJobSearch(position_name, city)
company_search = lagou.LagouCompanySearch()
company_full_name_list = []
for i in range(start, end):
    job_search.pn = i
    jobs = job_search.search_jobs()
    for job in jobs:
        # 写入文件company
        if (company_full_name_list.__contains__(job.company_full_name)):
            print(job.company_full_name + " 该公司已经搜索过，忽略")
            continue
        company_full_name_list.append(job.company_full_name)
        company_search.set_var(job)
        # 写入文件company
        company = company_search.search_company()
        if (company_search.is_waibao(company.desc)):
            print("-" * 20 + "start" + "-" * 20)
            print("发现外包公司：" + job.company_full_name)
            open("./waibao.txt", "a", encoding="utf-8").write(job.__str__() + "\n")
            # print(company.desc)
            print("-" * 20 + " end " + "-" * 20)

        else:
            open("./non-waibao.txt", "a", encoding="utf-8").write(job.__str__() + "\n")
