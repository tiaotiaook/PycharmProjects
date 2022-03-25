from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")


driver.find_elements_by_css_selector()

#
# bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
# print(link.text)

# logo = driver.find_element(By.CLASS_NAME,"python-logo")
# print(logo.size)
# search_bar = driver.find_element(By.NAME,"q")
# print(search_bar.tag_name)


# driver.get("https://www.amazon.com/Instant-Pot-60-Max-Electric/dp/B077T9YGRM/ref=sr_1_6?crid=CYPIGP4EQYLY&keywords=instant+pot&qid=1648132368&sprefix=%2Caps%2C1475&sr=8-6")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
#
#
# print(price.text)



# driver.close()
# driver.quit()

