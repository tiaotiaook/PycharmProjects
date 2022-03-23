from selenium import webdriver

chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com/Instant-Pot-60-Max-Electric/dp/B077T9YGRM/ref=sr_1_4?crid=BBI0WCRRRR2P&keywords=instant+pot&qid=1648055163&sprefix=instant%2Caps%2C1498&sr=8-4")
price = driver.find_element(by=By.Class,value="a-offscreen")
# _by_class_name("a-offscreen")

print(price.text)



# driver.close()
# driver.quit()

