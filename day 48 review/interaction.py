from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"

driver = webdriver.Chrome( executable_path=chrome_driver_path)


# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# print(driver.page_source)


# numbers =driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#
# print(numbers.text)

# number = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(number.text)
# number.click()

# find_element(By.LINK_TEXT,"...")寻找指定的链接
# Championship = driver.find_element(By.LINK_TEXT, "2021 World Snooker Championship")
# Championship.click()

# # 找到搜索栏
# search = driver.find_element(By.NAME, "search")
# # 输入要搜索的内容，但是还没有enter
# search.send_keys("python")
# # enter
# search.send_keys(Keys.ENTER)


# challenge
driver.get("http://secure-retreat-92358.herokuapp.com/")
print(driver.page_source)

search_1 = driver.find_element(By.NAME, "fName")
search_1.send_keys("tulong")

search_2 = driver.find_element(By.NAME, "lName")
search_2.send_keys("shaonv")

search_3 = driver.find_element(By.NAME, "email")
search_3.send_keys("1234566@gamil.com")

sign = driver.find_element(By.CSS_SELECTOR,"form button")
sign.click()






# driver.quit()


