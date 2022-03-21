from bs4 import BeautifulSoup
import requests

date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text,"html.parser")


song_names_spans = soup.find_all(name = "h3", class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                                     "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                                     "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                                     "u-max-width-230@tablet-only")
song_names = [song.getText() for song in song_names_spans]
print(song_names)
