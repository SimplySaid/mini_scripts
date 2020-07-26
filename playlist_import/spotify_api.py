import requests
import base64
import urllib.parse
import time
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

SPOTIFY_API_ENDPOINT = 'https://api.spotify.com/v1/'

CLIENT_ID = '738964632da7447a95a408902287a69e'
CLIENT_SECRET = '1139819a7d1b4f809986261bde0285b3'

class Spotify_API:
    def __init__ (self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.create_session()

        self.generate_access_token()

    def create_session(self, max_retries = 3, backoff_factor = 0.5):
        session = requests.session()
        retries = Retry(total = max_retries, backoff_factor = backoff_factor)
        session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session = session

    def generate_token(self):
        http_endpoint = 'https://accounts.spotify.com/authorize?client_id={}&response_type={}&redirect_uri={}'.format(self.client_id, 'code',urllib.parse.quote_plus('http://google.com'))
        print(http_endpoint)
        r = self.session.get(http_endpoint)
        print(r)
        self.headers = r

    def generate_access_token(self):
        client_creds = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()

        data = {
            "grant_type" : "client_credentials"
        }

        headers = {
            "Authorization" : f"Basic {client_creds}"
        }

        r = self.session.post("https://accounts.spotify.com/api/token", data = data, headers = headers)
        access_json = r.json()
        self.headers = {'Authorization': 'Bearer ' + access_json['access_token']}

    def http_request(self, http_endpoint, headers):
        r = self.session.get(http_endpoint, headers = headers)
        return r.json()

    def search_item (self, item, i_type):
        http_endpoint = SPOTIFY_API_ENDPOINT + 'search?q={}&type={}'.format(item.replace(' ','%20'),i_type)
        response = self.http_request(http_endpoint, self.headers)
        return response

spot_api = Spotify_API(CLIENT_ID, CLIENT_SECRET)
print(spot_api.search_item('Savoy & Bright Lights - The Wolf (Savoy Live Version)', 'track'))
#spot_api.generate_token()