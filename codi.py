# Codi 1
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

SPOTIPY_CLIENT_ID = 'a0f97f58de884da695b1e9df20ececa9'
SPOTIPY_CLIENT_SECRET = '84668a476d394a5fbc528a22d59a92d5'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist = '37i9dQZF1DWZYOM6QxgTaX'

# https://spotipy.readthedocs.io/en/2.22.1/spotipy.client.Spotify.playlist_items
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None)

relacions = []

for i in query["items"]:
    artists = i["track"]["artists"]

    for artist in artists:
        source_artist_name = artist["name"]
        source_artist_id = artist["id"]

        track_info = sp.track(i["track"]["id"])
        track_name = track_info["name"]
        album_name = track_info["album"]["name"]
        popularity = track_info["popularity"]
        release_date = track_info["album"]["release_date"]
        category = track_info["album"]["album_type"]

        artist_info = sp.artist(source_artist_id)
        genres = artist_info["genres"]

        relacions.append({
            "Canción": track_name,
            "Artista": source_artist_name,
            "ID del Artista": source_artist_id,
            "Popularidad": popularity,
            "Año de lanzamiento": release_date,
            "Álbum": album_name,
            "Categoría": category,
            "Géneros": genres
        })

df = pd.DataFrame(relacions)
df.to_csv('playlist.csv', index=False)

# Codi 2
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

SPOTIPY_CLIENT_ID = 'a0f97f58de884da695b1e9df20ececa9'
SPOTIPY_CLIENT_SECRET = '84668a476d394a5fbc528a22d59a92d5'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist = '37i9dQZF1DWZYOM6QxgTaX'

# https://spotipy.readthedocs.io/en/2.22.1/spotipy.client.Spotify.playlist_items
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None)

relacions = []

for i in query["items"]:
    artists = i["track"]["artists"]

    for artist in artists:
        source_artist_name = artist["name"]
        source_artist_id = artist["id"]

        if source_artist_name in ['Blaumut', 'The Tyets', 'Julieta', 'Figa Flawas', 'Ginestà', 'Suu']:
            track_info = sp.track(i["track"]["id"])
            track_name = track_info["name"]
            album_name = track_info["album"]["name"]
            popularity = track_info["popularity"]
            release_date = track_info["album"]["release_date"]
            category = track_info["album"]["album_type"]

            artist_info = sp.artist(source_artist_id)
            genres = artist_info["genres"]

            audio_features = sp.audio_features(i["track"]["id"])
            danceability = audio_features[0]["danceability"]

            relacions.append({
                "Canción": track_name,
                "Artista": source_artist_name,
                "ID del Artista": source_artist_id,
                "Popularidad": popularity,
                "Año de lanzamiento": release_date,
                "Álbum": album_name,
                "Categoría": category,
                "Géneros": genres,
                "Danceability": danceability
            })

df = pd.DataFrame(relacions)
df.to_csv('playlist.csv', index=False)
