from selenium import webdriver

chromedriver = "/Users/raghav/PycharmProjects/PythonSeleniumTesting/Chrome/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()

driver.get("https://tips2healthy.com")
driver.find_element_by_xpath("//ul[@id='cssnav']//a[contains(text(),'Home Remedies')]").click()
driver.find_elements_by_css_selector("status-msg-body").copy()
print(driver.title)
print(driver.current_url)
driver.back()
driver.find_element_by_id("Header1_headerimg").click()
driver.forward()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(3000)

driver.quit()



