from selenium import webdriver

from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"

driver = webdriver.Chrome( executable_path=chrome_driver_path)


driver.get("https://www.python.org/")

# print(driver.page_source)
#
# time_1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time')
# print(time_1.text)

times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")

# for time in times:
#     print(time.text)


names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

# for name in names:
#     print(name.text)

events={}

for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": names[n].text,
    }

print(events)


driver.quit()