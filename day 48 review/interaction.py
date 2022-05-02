from selenium import webdriver

from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"

driver = webdriver.Chrome( executable_path=chrome_driver_path)


driver.get("https://en.wikipedia.org/wiki/Main_Page")
# print(driver.page_source)


# numbers =driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#
# print(numbers.text)

number = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(number.text)


driver.quit()


