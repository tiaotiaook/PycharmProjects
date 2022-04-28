import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")


titles = soup.find_all(name="h3", class_="title")

# for title_name in titles:
#     print(title_name.getText())

title_list = [title_name.getText() for title_name in titles]
# print(title_list[::-1])
# for n in range(len(title_list)-1,-1,-1):
#     print(title_list[n])
title = title_list[::-1]
# print(title)

with open("moives.txt",mode = "w") as file:
    for title_film in title:
        file.write(f"{title_film}\n")

