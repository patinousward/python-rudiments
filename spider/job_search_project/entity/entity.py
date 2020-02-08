class JobInfo:
    @property
    def position_name(self):
        return self._position_name

    @position_name.setter
    def position_name(self, position_name):
        self._position_name = position_name

    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        self._position_id = position_id

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        self._company_id = company_id

    @property
    def company_full_name(self):
        return self._company_full_name

    @company_full_name.setter
    def company_full_name(self, company_full_name):
        self._company_full_name = company_full_name

    @property
    def company_short_name(self):
        return self._company_short_name

    @company_short_name.setter
    def company_short_name(self, company_short_name):
        self._company_short_name = company_short_name

    def __str__(self):  # 虽然没有写工资等信息，因为这个关键是用来过滤公司的，不是用来挑工作的脚本
        return str(self.position_id) + "," + self.position_name + "," + str(
            self.company_id) + "," + self.company_full_name + "," + self.company_short_name


class CompanyInfo:
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        self._company_id = company_id

    @property
    def company_full_name(self):
        return self._company_full_name

    @company_full_name.setter
    def company_full_name(self, company_full_name):
        self._company_full_name = company_full_name

    @property
    def company_short_name(self):
        return self._company_short_name

    @company_short_name.setter
    def company_short_name(self, company_short_name):
        self._company_short_name = company_short_name

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    def __str__(self):
        return str(self.company_id) + "," + self.company_full_name + "," + self.company_short_name
