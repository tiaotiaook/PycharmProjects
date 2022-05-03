from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "XXX"
ACCOUNT_PASSWORD = "XXX"
PHONE = "XXX"


chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"
driver = webdriver.Chrome( executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


sign_in_button = driver.find_element(By.LINK_TEXT, "登录")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID,"username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID,"password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)


time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()


time.sleep(5)
phone = driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)


submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()


# driver.quit()