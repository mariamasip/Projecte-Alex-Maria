# Explicació detallada del codi
### Codi 1: Extracció de dades de la llista IndieCat
Aquest codi utilitza la llibreria Spotipy per interactuar amb l'API de la plataforma de música, Spotify. Bàsicament, obté les dades d'una llista de reproducció específica i en crea un fitxer CSV que conté informació sobre les cançons, artistes i altres detalls relacionats. És necessari proporcionar les credencials del client de Spotify per autenticar-se i accedir a aquestes dades.

```Python
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

# Credencials del client de Spotify
SPOTIPY_CLIENT_ID = 'XXXXX'
SPOTIPY_CLIENT_SECRET = 'XXXXX'

# Inicialitza l'autenticació amb les credencials del client de Spotify
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Identificador de la llista de reproducció
playlist = '37i9dQZF1DWZYOM6QxgTaX'

# Obté els elements de la llista de reproducció utilitzant l'API de Spotify
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None)

# Llista buida per emmagatzemar les relacions d'artistes i cançons
relacions = []

# Recorre tots els elements de la llista de reproducció
for i in query["items"]:
    artists = i["track"]["artists"]

    # Recorre tots els artistes associats a cada cançó
    for artist in artists:
        source_artist_name = artist["name"]
        source_artist_id = artist["id"]

        # Obté informació de la cançó
        track_info = sp.track(i["track"]["id"])
        track_name = track_info["name"]
        album_name = track_info["album"]["name"]
        popularity = track_info["popularity"]
        release_date = track_info["album"]["release_date"]
        category = track_info["album"]["album_type"]

        # Obté informació de l'artista
        artist_info = sp.artist(source_artist_id)
        genres = artist_info["genres"]

        # Afegeix les relacions a la llista
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

# Crea un DataFrame a partir de les relacions
df = pd.DataFrame(relacions)

# Exporta el DataFrame a CSV
df.to_csv('playlist.csv', index=False)

```
### Codi 2: Extracció de dades fora de la llista
Aquest segon codi és una versió ampliada del codi anterior, amb la següent modificació;
S'afegeix una comprovació per verificar si l'artista de cada cançó es troba e la llista ('Blaumut', 'The Tyets', 'Julieta', 'Figa Flawas', 'Ginestà', 'Suu').
Si l'artista està dins la llista, s'obté informació addicional sobre la cançó fora de la llista, com ara les característiques de l'àudio, les seves cançons més populars, etc. S'afegeixen a la llista de relacions com un diccionari per finalment, crear un DataFrame de Pandas i es guarda com un fitxer CSV anomenat 'playlist.csv'.

```Python
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

# Configuració de les credencials del client de Spotify
SPOTIPY_CLIENT_ID = 'XXXXX'
SPOTIPY_CLIENT_SECRET = 'XXXXX'

# Autenticació amb les credencials del client de Spotify
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Identificador de la llista de reproducció
playlist = '37i9dQZF1DWZYOM6QxgTaX'

# Obtenir informació de les cançons de la llista de reproducció
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None)

# Llista per emmagatzemar les relacions de les cançons i artistes
relacions = []

# Recórrer cada ítem de la resposta de la consulta
for i in query["items"]:
    artists = i["track"]["artists"]

    # Recórrer cada artista de la cançó
    for artist in artists:
        source_artist_name = artist["name"]
        source_artist_id = artist["id"]

        # Comprovar si l'artista està a la llista 
        if source_artist_name in ['Blaumut', 'The Tyets', 'Julieta', 'Figa Flawas', 'Ginestà', 'Suu']:
            # Obtindre informació de la cançó
            track_info = sp.track(i["track"]["id"])
            track_name = track_info["name"]
            album_name = track_info["album"]["name"]
            popularity = track_info["popularity"]
            release_date = track_info["album"]["release_date"]
            category = track_info["album"]["album_type"]

            # Obtindre informació de l'artista
            artist_info = sp.artist(source_artist_id)
            genres = artist_info["genres"]

            # Obtindre característiques de la cançó
            audio_features = sp.audio_features(i["track"]["id"])
            danceability = audio_features[0]["danceability"]

            # Afegir les dades a la llista de relacions
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

# Crear un DataFrame a partir de les relacions
df = pd.DataFrame(relacions)

# Exportar el DataFrame com a un fitxer CSV
df.to_csv('playlist.csv', index=False)

```
