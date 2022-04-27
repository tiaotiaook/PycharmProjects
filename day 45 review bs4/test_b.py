from bs4 import BeautifulSoup
import requests

URL = "https://www.bilibili.com/v/popular/rank/all"

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")


titles = soup.find_all(name="a", class_="title")


for title_name in titles:
    # print(title_name)
    URL_1 = str("https:") + str(title_name.get("href"))
    print(URL_1)
    print(title_name.getText())

    response_1 = requests.get(URL_1)
    content_1 = response_1.text

    soup_1 = BeautifulSoup(content_1, "html.parser")

    bofang = soup_1.find(name = "span", class_ = "view").getText()
    print(bofang)

    # bofang_0 = soup_1.find ( name="span", class_="view-count" ).getText ()
    # print ( bofang_0 )

    print("====分割线====")









# from bs4 import BeautifulSoup
# import requests
#
# URL = "//www.bilibili.com/video/BV1rr4y1b7sz"
#
# response = requests.get(URL)
# content = response.text
#
# soup = BeautifulSoup(content, "html.parser")
#
# print(soup)