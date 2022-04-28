from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)


soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name='h3', class_="a-no-trucate")
for song in songs:
    print(song.getText())




# client_id = "3fd0b6ede06a4917909eea124dcd69f4"
#
# client_secret="33460cf620f342b8a75263e8bee3a598"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://tiaotiao.com/callback/",
        client_id="3fd0b6ede06a4917909eea124dcd69f4",
        client_secret="33460cf620f342b8a75263e8bee3a598",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]



