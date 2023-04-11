#Link to spotify data. 
import time

client_id="6ad5ca213ff548cd98d1d1ebb7488244"
client_secret="4e5bf2f4af4e466fb4468617a19b3722"

import requests
import json




# Set up authentication credentials

auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})
auth_response_data = json.loads(auth_response.text)
access_token = auth_response_data['access_token']

# Set up API request
url = 'https://api.spotify.com/v1/recommendations'
headers = {'Authorization': 'Bearer ' + access_token}
params = {
    'limit': 100,
    'market': 'US',
    'seed_artsits':'4NHQUGzhtTLFvgF5SZesLK',
    'seed_genres': 'country' ,
    'seed_tracks' : '0c6xIDDpzE81m2q797ordA'

}


def get_song_attributes(song_id):
    # Set up the Spotify API endpoint and headers
    SPOTIFY_API_ENDPOINT = 'https://api.spotify.com/v1/audio-features/'
    headers = {'Authorization': 'Bearer ' + access_token}

    # Make API request to get song attributes
    response = requests.get(SPOTIFY_API_ENDPOINT + song_id, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        # data=data["audio_features"]
        attributes = {
            'Danceability': data['danceability'],
            'Energy': data['energy'],
            'Loudness': data['loudness'],
            'Acousticness': data['acousticness'],
            'Instrumentalness': data['instrumentalness'],
            'Liveness': data['liveness'],
            'Speechiness': data['speechiness'],
            'Tempo': data['tempo'],
            'Key': data['key'],
            'Mode': data['mode']
        }

        return attributes
    else:
        print(f'Request failed with status code {response.status_code}: {response.text}')
        return None
    


# Make API request and process response
response = requests.get(url, headers=headers, params=params)
if response.status_code == 100:
    data = json.loads(response.text)

    # Process data as needed
    attributes_list = []
    for value in data['tracks']:
        pass
        # song_id = value['id']
        # name = value['name']
        # attributes_list.append(song_id , name)
        
    print(attributes_list)
    
else:
    print(f'Request failed with status code {response.status_code}: {response.text}')




#For each value , get song attributes. 











