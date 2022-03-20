from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# NOTE - must enter information below for code to work
CLIENT_ID = "xxxxxxxxxxxxxxxxxxxxxxx"
CLIENT_SECRET = "xxxxxxxxxxxxxxxxxxxxxxx"
USER_ID = "xxxxxxxxxxxxxx"

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com"))

# Ask for which year the user wishes to get the billboard hits
date = input("what year you would like to travel to? Please type the date in the YYYY-MM-DD format: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

# get soup 
website_data = response.text
soup = BeautifulSoup(website_data, "html.parser")

# check soup results
# print(soup.prettify())

# get song titles out of scraped data
song_titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
final_titles = [title.getText() for title in song_titles]

# check scraped song titles
# print(final_titles)

# get artists out of scraped data
artists = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")
final_artists = [artist.getText() for artist in artists]

# check scraped artists
# print(final_artists)

music_info = zip(final_artists, final_titles)
search_criteria = set(music_info)
# print(search_criteria)

# search Spotify for scraped artists and song titles and add track IDs to a results list
uri_list = []
for artist, track in search_criteria:
    results = sp.search(q=f"artist:{artist} track:{track}", type="track")
    try:
        uri_list.append(results["tracks"]["items"][0]["id"])
    except IndexError:
        pass

# check uri list
# print(len(uri_list))

# create new private Spotify playlist using Spotipy
my_playlist = sp.user_playlist_create(user=USER_ID, name=f"{date} Billboard 100", public="false")

playlist_id = my_playlist["id"]

# add results to Spotify playlist
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
