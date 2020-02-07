class AbstractJobSearch:

    def __init__(self, job_position="大数据开发", city="深圳", pn=1):
        self._job_position = job_position
        self._city = city
        self._pn = pn

    @property
    def pn(self):
        return self._pn

    @pn.setter
    def pn(self, pn):
        self._pn = pn

    @property
    def job_position(self):
        return self._job_position  # _表示不希望外部直接进行赋值的属性名，不单单只是起警告作用，

    @job_position.setter  # 需要配合@property进行使用
    def job_position(self, job_position):
        self._job_position = job_position

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    def search_jobs(self):  # ->对参数的返回值进行指定,但是只能指定基本类型
        # 子类调用search方法
        # 对返回的text进行解析（本类中去解析）
        pass

    #
    def job_info_parser(self):
        pass
