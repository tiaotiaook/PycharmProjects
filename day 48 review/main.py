from selenium import webdriver

chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

# 关闭页面
driver.close()
# 退出浏览器
driver.quit()