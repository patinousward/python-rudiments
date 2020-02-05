from selenium import webdriver

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.lagou.com/gongsi/378796.html")
    try:
        driver.find_element_by_xpath("//*[@class='text_over']").click()
    except BaseException:
        pass
    contents = driver.find_elements_by_xpath("//*[@class='company_content']/p")
    for content in contents:
        print(content.text)
