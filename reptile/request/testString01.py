from selenium import webdriver
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.lagou.com/gongsi/92075.html')
    contents = driver.find_elements_by_xpath("//*[@class='company_content']/p")
    for content in contents:
        print(content.text)