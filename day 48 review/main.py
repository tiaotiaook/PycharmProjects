from selenium import webdriver
from selenium.webdriver.common.by import By


chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())


chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_2?crid=14HIQM0GBAAEF&keywords=instant+pot&qid=1651248791&sprefix=instant+pot+t%2Caps%2C655&sr=8-2")


price = driver.find_element(By.CLASS_NAME, "a-offscreen")


print(price.text)

# 关闭页面
# driver.close()
# 退出浏览器
driver.quit()