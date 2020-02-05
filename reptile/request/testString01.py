from selenium import webdriver

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.lagou.com/gongsi/691605.html")
    try:
        driver.find_element_by_xpath("//*[@class='text_over']").click()
    except BaseException:
        pass
    spanText = driver.find_element_by_xpath("//*[@class='company_content']").text
    print(spanText)
    pTexts = driver.find_elements_by_xpath("//*[@class='company_content']/p")
    for pText in pTexts:
        print(pText.text)
