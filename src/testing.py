import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.client import Spotify

SPOTIPY_CLIENT_ID = 'eaef1e6ac22344f181edd44e36a48863'
SPOTIPY_CLIENT_SECRET = '9b8ae1b5beed43bc9b210ac263b327ba'

mySpotipyClient = Spotify(object)
mySpotipy = SpotifyClientCredentials()
mySpotipy.init(self, SPOTIPY_ClIENT_ID, SPOTIPY_CLIENT_SECRET, None)

mySpotipy.get_access_token(self) 

