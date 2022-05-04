from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

# print(all_links)
# print(len(all_links))

all_address_elements =soup.select(".list-card-addr")
all_address = []
for address in all_address_elements:
    all_address.append(address.get_text().split(" | ")[-1])

# print(all_address)
# print(len(all_address))

all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        # print('Multiple listings for the card')
        # # Price with multiple listings
        # price = element.select(".list-card-details li")[0].contents[0]
        pass
    finally:
        all_prices.append(price)

# print(all_prices)
# print(len(all_prices))

chrome_driver_path = "/Users/2shihua1yin/Desktop/Web Development/chromedriver 2"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_links)):

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSckArxIABU2pbcGNx6dmk2tZN5H2txoKRf24Vod2zSi8ze1bw/viewform?usp=sf_link")
    time.sleep ( 2 )
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input' )
    price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input' )
    link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input' )
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div' )


    address.send_keys(all_address[n])
    price.send_keys ( all_prices[n] )
    link.send_keys ( all_links[n] )
    submit_button.click ()

