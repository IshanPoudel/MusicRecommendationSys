import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up authorization with your client ID and secret
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for a track by name
track_name = 'Billie Jean'
results = sp.search(q=track_name, type='track', limit=1)

# Print out some information about the track
track = results['tracks']['items'][0]
print('Track name:', track['name'])
print('Artist:', track['artists'][0]['name'])
print('Album:', track['album']['name'])
print('Duration (ms):', track['duration_ms'])
