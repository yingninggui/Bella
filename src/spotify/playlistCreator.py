#imports
import os
import sys
import spotipy
import client
import random
import json
import pprint
import spotipy.util as util 
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.client import Spotify

#administrative 
SPOTIPY_CLIENT_ID = 'eaef1e6ac22344f181edd44e36a48863'
SPOTIPY_CLIENT_SECRET = '9b8ae1b5beed43bc9b210ac263b327ba'
username = '22twkvspkih7nwqom5dlty3hi'

client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
#print(client_credentials_manager.get_access_token())
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

user = sp.user(username)
pprint.pprint(user)
playlists = sp.user_playlists(username)
sp.user_playlist_tracks(user)
for playlist in playlists['items']:
   print(playlist['name'])

   results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
   tracks = results['tracks']
   while tracks['next']:
      tracks = sp.next(tracks)

#blues playlist to list 
uriBlues = 'spotify:user:spotify:playlist:37i9dQZF1DX2iUghHXGIjj'
playlist_id = uriBlues.split(':')[4]
results = sp.user_playlist('spotify', playlist_id, fields="tracks,next")
blues = results['tracks']
while blues['next']:
    blues = sp.next(blues)
#blues = sp.playlist(playlist_id)
bluesrandom = random.SystemRandom()

#will this work ever
##def show_tracks(tracks):
##    for i, item in enumerate(tracks['items']):
##        track = item['track']
##        print "   %d %32.32s %s" % (i, track['artists'][0]['name'],track['name'])

#chill playlist to list 
uriChill= 'spotify:user:majesticcasualofficial:playlist:6wjCvkAFovrVIRM8VfZLZG'
playlist_id = uriChill.split(':')[4]
##results = sp.user_playlist('majesticcasualofficial', playlist_id, fields="tracks,next")
##chill = results['tracks']
##while chill['next']:
##    chill = sp.next(chill)
###chill = sp.playlist(playlist_id)
##chillrandom = random.SystemRandom()

#classical playlist to list 
uriClassical = 'spotify:user:spotify:playlist:37i9dQZF1DWWEJlAGA9gs0'
playlist_id = uriClassical.split(':')[4]
results = sp.user_playlist('spotify', playlist_id, fields="tracks,next")
classical = results['tracks']
while classical['next']:
    classical = sp.next(classical)
#classical = sp.playlist( playlist_id)
classicalrandom = random.SystemRandom()

#country playlist to list 
uriCountry = 'spotify:user:spotify:playlist:37i9dQZF1DWYV2Gh2QglGo'
playlist_id = uriCountry.split(':')[4]
results = sp.user_playlist('spotify', playlist_id, fields="tracks,next")
country = results['tracks']
while country['next']:
    country = sp.next(country)
#country = sp.playlist(playlist_id)
countryrandom = random.SystemRandom()

#eletronic/dance playlist to list 
uriEdm = 'spotify:user:verts87:playlist:1M55NZEq0b79IhafDd9UP0'
playlist_id = uriEdm.split(':')[4]
results = sp.user_playlist('verts87', playlist_id, fields="tracks,next")
edm = results['tracks']
while edm['next']:
    edm = sp.next(edm)
#edm = sp.playlist(playlist_id)
edmrandom = random.SystemRandom()

#hip-hop playlist to list 
uriHiphop = 'spotify:user:spotify:playlist:37i9dQZF1DWY4xHQp97fN6'
playlist_id = uriHiphop.split(':')[4]
results = sp.user_playlist('spotify', playlist_id, fields="tracks,next")
hiphop = results['tracks']
while hiphop['next']:
    hiphop = sp.next(hiphop)
#hiphop = sp.playlist(playlist_id)
hiphoprandom = random.SystemRandom()

#pop playlist to list 
uriPop = 'spotify:user:spotify:playlist:37i9dQZF1DXarRysLJmuju'
playlist_id = uriPop.split(':')[4]
results = sp.user_playlist('spotify', playlist_id, fields="tracks,next")
pop = results['tracks']
while pop['next']:
    pop = sp.next(pop)
#pop = sp.playlist(playlist_id)
poprandom = random.SystemRandom()

#rock laylist to list 
uriRock = 'spotify:user:spotify:playlist:37i9dQZF1DWXRqgorJj26U'
playlist_id = uriRock.split(':')[4]
results = sp.user_playlist('spotify', playlist_id, fields="tracks,next")
rock = results['tracks']
while rock['next']:
    rock = sp.next(rock)
#rock = sp.playlist(playlist_id)
rockrandom = random.SystemRandom()

#romance playlist to list 
uriRomance = 'spotify:user:spotify:playlist:37i9dQZF1DX5IDTimEWoTd'
playlist_id = uriRomance.split(':')[4]
results = sp.user_playlist('majesticcasualofficial', playlist_id, fields="tracks,next")
romance = results['tracks']
while romance['next']:
    romance = sp.next(romance)
#romance = sp.playlist(playlist_id)
romancerandom = random.SystemRandom() 

case = raw_input()
myPlaylist = [] 

while true:
    
    #blues 
    if (case==0):
        song = bluesrandom.choice(blues); 
        myPlaylist.append(song)
        
    #chill
    elif(case==1):
        song = chillsrandom.choice(blues); 
        myPlaylist.append(song)
        
    #classical 
    elif(case==2):
        song = classicalrandom.choice(blues); 
        myPlaylist.append(song)
        
    #country 
    elif(case==3):
        song = countryrandom.choice(blues); 
        myPlaylist.append(song)
        
    #electronic/dance 
    elif(case==4):
        song = edm.choice(blues); 
        myPlaylist.append(song)
        
    #hip-hop
    elif(case==5):
        song = hiphoprandom.choice(blues); 
        myPlaylist.append(song)
        
    #pop 
    elif(case==6):
        song = poprandom.choice(blues); 
        myPlaylist.append(song)
        
    #rock 
    elif(case==7):
        song = rockrandom.choice(blues); 
        myPlaylist.append(song)
        
    #romance 
    elif(case==8):
        song = romancerandom.choice(blues); 
        myPlaylist.append(song)
        
    else:
        break;

#take category and find a seed song
#add music, 9 switch statements

