import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

SPOTIFY_API_ENDPOINT = 'https://api.spotify.com/v1/'

CLIENT_ID = '738964632da7447a95a408902287a69e'
CLIENT_SECRET = '1139819a7d1b4f809986261bde0285b3'

class Spotify_API:
    def __init__ (self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.headers = {'Authorization': 'Bearer '  + self.client_secret}

        print(self.headers)

        self.create_session()

    def create_session(self, max_retries = 3, backoff_factor = 0.5):
        session = requests.session()
        retries = Retry(total = max_retries, backoff_factor = backoff_factor)
        session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session = session

    def generate_

    def http_request(self, http_endpoint, headers):
        r = self.session.get(http_endpoint, headers = headers)
        return r.json()


    def search_song (self, song):
        http_endpoint = SPOTIFY_API_ENDPOINT + 'search?q={}'
        response = self.http_request(http_endpoint, self.headers)
        return response

spot_api = Spotify_API(CLIENT_ID, CLIENT_SECRET)
print(spot_api.search_song('Lonely'))