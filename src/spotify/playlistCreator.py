#imports
import os 
import spotipy
import util
import oauth2
import client
import random
import json
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.client import Spotify

#administrative 
SPOTIPY_CLIENT_ID = 'eaef1e6ac22344f181edd44e36a48863'
SPOTIPY_CLIENT_SECRET = '9b8ae1b5beed43bc9b210ac263b327ba'

#is this even necessary tbh 
mySpotipyClient = Spotify(object)
mySpotipy = SpotifyClientCredentials()
mySpotipy.init(self, SPOTIPY_ClIENT_ID, SPOTIPY_CLIENT_SECRET, None)
mySpotipy.get_access_token(self)

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#blues playlist to list 
uriBlues = 'spotify:user:spotify:playlist:37i9dQZF1DX2iUghHXGIjj'
playlist_id = uriBlues.split(':')[4]
blues = sp.playlist( playlist_id)
bluesrandom = random.SystemRandom()

#chill playlist to list 
uriChill= 'spotify:user:majesticcasualofficial:playlist:6wjCvkAFovrVIRM8VfZLZG'
playlist_id = uriBlues.split(':')[4]
chill = sp.playlist( playlist_id)
chillrandom = random.SystemRandom()

#classical playlist to list 
uriClassical = 'spotify:user:spotify:playlist:37i9dQZF1DWWEJlAGA9gs0'
playlist_id = uriBlues.split(':')[4]
classical = sp.playlist( playlist_id)
classicalrandom = random.SystemRandom()

#country playlist to list 
uriCountry = 'spotify:user:spotify:playlist:37i9dQZF1DWYV2Gh2QglGo'
playlist_id = uriBlues.split(':')[4]
country = sp.playlist( playlist_id)
countryrandom = random.SystemRandom()

#eletronic/dance playlist to list 
uriEdm = 'spotify:user:verts87:playlist:1M55NZEq0b79IhafDd9UP0'
playlist_id = uriBlues.split(':')[4]
edm = sp.playlist( playlist_id)
edmrandom = random.SystemRandom()

#hip-hop playlist to list 
uriHiphop = 'spotify:user:spotify:playlist:37i9dQZF1DWY4xHQp97fN6'
playlist_id = uriBlues.split(':')[4]
hiphop = sp.playlist( playlist_id)
hiphoprandom = random.SystemRandom()

#pop playlist to list 
uriPop = 'spotify:user:spotify:playlist:37i9dQZF1DXarRysLJmuju'
playlist_id = uriBlues.split(':')[4]
pop = sp.playlist( playlist_id)
poprandom = random.SystemRandom()

#rock laylist to list 
uriRock = 'spotify:user:spotify:playlist:37i9dQZF1DWXRqgorJj26U'
playlist_id = uriBlues.split(':')[4]
rock = sp.playlist( playlist_id)
rockrandom = random.SystemRandom()

#romance playlist to list 
uriRomance = 'spotify:user:spotify:playlist:37i9dQZF1DX5IDTimEWoTd'
playlist_id = uriBlues.split(':')[4]
romance = sp.playlist( playlist_id)
romancerandom = random.SystemRandom() 

mood = #max's input
myPlaylist = [] 

while true:
    
    #blues 
    if (case==0):
        song = bluesrandom.choice(blues); 
        myPlaylist.append(song)
        
    #chill
    elif(case==1):
        song = sp.search(q=genre)
        myPlaylist.append(song)
        
    #classical 
    elif(case==2):
        song = sp.search(q=genre)
        myPlaylist.append(song)
        
    #country 
    elif(case==3):
        song = sp.search(q=genre)
        myPlaylist.append(song)
        
    #electronic/dance 
    elif(case==4):
        song = sp.search(q=genre)
        myPlaylist.append(song)
        
    #hip-hop
    elif(case==5):
        song = sp.search(q=genre)
        myPlaylist.append(song)
        
    #pop 
    elif(case==6):
        song = sp.search(q=genre)
        myPlaylist.append(song)
        
    #rock 
    elif(case==7):
        song = sp.search(q=genre)
        myPlaylist.append(song)
        
    #romance 
    elif(case==8):
        song = sp.search(q=genre)
        
    else:
        break; 

while true:
    addSong(mood);

#take category and find a seed song
#add music, 9 switch statements

