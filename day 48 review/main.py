from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = '/path/to/chromedriver'

chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"

driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

# driver.get("https://www.baidu.com/")
driver.get("https://www.python.org/")
# print(driver.page_source)
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME,"python")
# print(logo.size)
#
# documentation_link = driver.find_elements_by_css_selector(".documentation-widget a")


bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

doc_link =driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[3]/p[2]/a')
print(doc_link.text)

test_1 = driver.find_element(By.XPATH, '//*[@id="container"]/li[4]/ul/li[13]/a')
print(test_1.text)

# documentation_link = driver.find_elements(By.CSS_SELECTOR,".documentation-widget a")
# # documentation_link = driver.find_elements_by_css_selector(".documentation-widget a")
# print(documentation_link)
# print(documentation_link.text)
# chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_2?crid=14HIQM0GBAAEF&keywords=instant+pot&qid=1651248791&sprefix=instant+pot+t%2Caps%2C655&sr=8-2")
# print("Debug: begin to crawling...")
# print(driver.page_source)
#


# 关闭页面
# driver.close()
# 退出浏览器
driver.quit()