class AbstractCompanySearch:
    keys = ["外包", "IT服务提供商","解决方案提供商","软件"]

    def search_company(self):
        pass

    def company_info_parser(self, response):
        pass

    def set_var(self, var):
        pass

    def is_waibao(self, desc: str):
        flag = False
        for key in self.keys:
            if (desc.__contains__(key)):
                flag = True
        return flag
