#imports
import os
import sys
import spotipy
import client
import random
import pprint
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.client import Spotify

#administrative
import json
from flask import Flask, request, redirect, g, render_template
import requests
import base64
from urlparse import urlparse


CLIENT_ID = "eaef1e6ac22344f181edd44e36a48863"
CLIENT_SECRET = "9b8ae1b5beed43bc9b210ac263b327ba"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = '22twkvspkih7nwqom5dlty3hi'
playlist_id2 = '7yBfj4J84zawKqvqbDTVGc'
playlist_id = '5g4u6my7planc05uGHcHr1'
track_ids = sp.user_playlist_tracks('22twkvspkih7nwqom5dlty3hi',playlist_id2)[u'items'][0][u'track'][u'id']

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)



sp = spotipy.Spotify(auth=token)
sp.trace = False
results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
