from selenium import webdriver

chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com")
# driver.close()
driver.quit()

