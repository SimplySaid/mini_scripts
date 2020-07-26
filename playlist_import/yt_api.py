import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLMvaT-Nb9FtRd2nqswRzG36GpDm8yvWdC"
YT_DATA_V3_ENDPOINT = "https://www.googleapis.com/youtube/v3/"

API_KEY = 'AIzaSyBaYnJgZnSIV4b4rxQ4zlWgoXKLFkaww9c'

class YT_DATA_API:
    def __init__ (self, api_key, api_version = 3):
        self.api_key = api_key
        self.api_version = api_version

        self.create_session()
    
    def create_session(self, max_retries = 3, backoff_factor = 0.5):
        session = requests.session()
        retries = Retry(total = max_retries, backoff_factor = backoff_factor)
        session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session = session

    def http_request(self, http_endpoint):
        r = self.session.get(http_endpoint)
        return r.json()

    def get_id_by_user_name(self, user, **kwargs):
        http_endpoint = YT_DATA_V3_ENDPOINT + "channels?key={}&forUsername={}&part=id".format(self.api_key, user)
        response = self.http_request(http_endpoint)
        try:
            return response['items'][0]['id']
        except:
            return 'Invalid User ID'

    def get_user_playlists(self, channel_id, next_page_token = False, **kwargs):
        playlists = []
        while True:
            http_endpoint = YT_DATA_V3_ENDPOINT + "playlists?key={}&channelId={}&part=id".format(self.api_key,channel_id)
            for k,v in kwargs.items():
                http_endpoint += '&{}={}'.format(k,v)

            if next_page_token:
                http_endpoint += "&pageToken={}".format(next_page_token)

            response = self.http_request(http_endpoint)
            if response.get('items'):
                for item in response.get('items'):
                    playlists.append(item['id'])
            if response.get('nextPageToken'):
                next_page_token = response.get('nextPageToken')
            else:
                break
        return playlists

    def get_playlist_videos(self, playlist_id, next_page_token = False, **kwargs):
        videos = []
        while True:
            http_endpoint = YT_DATA_V3_ENDPOINT + "playlistItems?part=snippet&playlistId={}&maxResults=50&key={}".format(playlist_id,self.api_key)
            for k,v in kwargs.items():
                http_endpoint += '&{}={}'.format(k,v)
            
            if next_page_token:
                http_endpoint += "&pageToken={}".format(next_page_token)

            response = self.http_request(http_endpoint)
            if response.get('items'):
                for item in response.get('items'):
                    videos.append(item['snippet']['title'])
            if response.get('nextPageToken'):
                next_page_token = response.get('nextPageToken')
            else:
                break
        return videos

    def get_playlist_id(self, channel_url):
        return

yt_api = YT_DATA_API(API_KEY)
user_id = yt_api.get_id_by_user_name('TrU3Ta1ent')
#print(yt_api.get_user_playlists(user_id, kwargs = {'maxResults':50}))

print(yt_api.get_playlist_videos('PLMvaT-Nb9FtRd2nqswRzG36GpDm8yvWdC',kwargs = {'maxResults':50}))