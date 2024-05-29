from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Please type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{URL}{date}/")
billboard_hot_webpage = response.text

soup = BeautifulSoup(billboard_hot_webpage, "html.parser")
hot_list = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in hot_list]
pprint(song_titles)

# ----------------------------- SPOTIFY AUTHENTICATION------------------------------- #
CLIENT_ID = os.environ.get("YOUR_CLIENT_ID")
CLIENT_SECRET = os.environ.get("YOUR_CLIENT_SECRET")
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ.get("YOUR_USERNAME"),
    )
)
------------------ CREATE A SPOTIFY PLAYLIST FROM BILLBOARD WEBPAGE----------------- #
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(f"Track: {song} year: {year}", type="track", limit=1, market="US")
    # print(result)

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

------------------ CREATING AND ADDING TO SPOTIFY PLAYLIST-----------------
my_spotify_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=my_spotify_playlist["id"], items=song_uris)
