import requests
import json

# Set up authentication credentials
auth_url = 'https://accounts.spotify.com/api/token'
client_id="6ad5ca213ff548cd98d1d1ebb7488244"
client_secret="4e5bf2f4af4e466fb4468617a19b3722"
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
    'limit': 10,
    'market': 'US',
    'seed_artists': '0LcJLqbBmaGUft1e9Mm8HV',  # artist ID
    'seed_genres': 'pop',
    'seed_tracks': '1M0rBi5x8U5WfxzDJH0TuC'  # track ID
}

# Make API request and process response
response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    data = json.loads(response.text)
    # Process data as needed
else:
    print(f'Request failed with status code {response.status_code}: {response.text}')

# Extract ID and name for each recommended song
for track in data['tracks']:
    print(f"ID: {track['id']}, Name: {track['name']}")
