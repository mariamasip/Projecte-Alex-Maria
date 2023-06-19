Aquest codi utilitza la llibreria Spotipy per interactuar amb l'API de Spotify. Bàsicament, obté les dades d'una llista de reproducció específica i en crea un fitxer CSV que conté informació sobre les cançons, artistes i altres detalls relacionats. És necessari proporcionar les credencials del client de Spotify per autenticar-se i accedir a les dades.

```Python
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

# Credencials del client de Spotify
SPOTIPY_CLIENT_ID = 'a0f97f58de884da695b1e9df20ececa9'
SPOTIPY_CLIENT_SECRET = '84668a476d394a5fbc528a22d59a92d5'

# Inicialitza l'autenticació amb les credencials del client de Spotify
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Identificador de la llista de reproducció desitjada
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

# Exporta el DataFrame a un fitxer CSV
df.to_csv('playlist.csv', index=False)

```

Aquest segon codi és una versió ampliada del codi anterior, amb la següent modificació;
S'afegeix una comprovació per verificar si l'artista de cada cançó es troba en una llista determinada ('Blaumut', 'The Tyets', 'Julieta', 'Figa Flawas', 'Ginestà', 'Suu').
Aquesta comprovació es fa utilitzant una declaració if. Si l'artista està en la llista, s'obté informació addicional sobre la cançó, com ara les característiques de l'àudio (en aquest cas, només es pren la "danceability").Les dades de la cançó, l'artista, les característiques de l'àudio i altres detalls s'afegeixen a la llista de relacions com un diccionari. Finalment, es crea un DataFrame de Pandas a partir de les relacions i es guarda com un fitxer CSV anomenat 'playlist.csv', sense incloure l'índex.

```Python
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

# Configuració de les credencials del client de Spotify
SPOTIPY_CLIENT_ID = 'a0f97f58de884da695b1e9df20ececa9'
SPOTIPY_CLIENT_SECRET = '84668a476d394a5fbc528a22d59a92d5'

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

        # Comprovar si l'artista està en una llista determinada
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

            # Obtindre característiques de l'àudio de la cançó
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
