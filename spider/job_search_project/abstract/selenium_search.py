import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from spider.job_search_project.abstract.search import Search


class Seleniumsearch(Search):
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=chrome_options)

    def search(self):
        self.driver.get(self.get_requesst_url())
        time.sleep(5)  # 必须
        # 等待页面加载完成
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.getWaitLoadedXPATH()))
        )

    def get_requesst_url(self):
        pass

    def getWaitLoadedXPATH(self):
        pass

    def close(self):
        print("driver is closing")
        self.driver.close()
        print("driver is closed")
