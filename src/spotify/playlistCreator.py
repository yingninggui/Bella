#imports
import os
import sys
import spotipy
import client
import random
import pprint
import spotipy.util as util
import time
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.client import Spotify
import json
from flask import Flask, request, redirect, g, render_template
import requests
import base64
from urlparse import urlparse
import run

CLIENT_ID = "eaef1e6ac22344f181edd44e36a48863"
CLIENT_SECRET = "9b8ae1b5beed43bc9b210ac263b327ba"


username = '22twkvspkih7nwqom5dlty3hi'
scope = 'playlist-modify-public'

muse = run.MuseServer()

token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost:8000/callback/')
sp = spotipy.Spotify(auth=token)
uri2 = 'spotify:user:22twkvspkih7nwqom5dlty3hi:playlist:5g4u6my7planc05uGHcHr1'
playlist_id2 = uri2.split(':')[4]

def addSong(track_id):
    sp.user_playlist_add_tracks(username, playlist_id2,track_id)

def addNext(track_id):
    oldTrack=[]
    oldTrack.append(sp.user_playlist_tracks(username, playlist_id2)[u'items'][len(sp.user_playlist_tracks(username, playlist_id2)[u'items'])-1][u'track'][u'uri'])
    sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id2, oldTrack)
    sp.user_playlist_add_tracks(username, playlist_id2, track_id)


case = muse.get_curr_song_type()
uriBlues = 'spotify:user:spotify:playlist:37i9dQZF1DX2iUghHXGIjj'
playlist_blues = uriBlues.split(':')[4]
lengthBlues = sp.user_playlist_tracks('spotify', playlist_blues)[u'items']
songsBlues = []
for i in range(len(lengthBlues)):
    songsBlues.append(sp.user_playlist_tracks('spotify', playlist_blues)[u'items'][i][u'track'][u'uri'])

uriChill = 'spotify:user:majesticcasualofficial:playlist:6wjCvkAFovrVIRM8VfZLZG'
playlist_chill = uriChill.split(':')[4]
lengthChill = sp.user_playlist_tracks('majesticcasualofficial', playlist_chill)[u'items']
songsChill = []
for i in range(len(lengthChill)):
    songsChill.append(sp.user_playlist_tracks('majesticcasualofficial', playlist_chill)[u'items'][i][u'track'][u'uri'])

uriClassical = 'spotify:user:spotify:playlist:37i9dQZF1DWWEJlAGA9gs0'
playlist_classical = uriClassical.split(':')[4]
lengthClassical = sp.user_playlist_tracks('spotify', playlist_classical)[u'items']
songsClassical = []
for i in range(len(lengthClassical)):
    songsClassical.append(sp.user_playlist_tracks('spotify', playlist_classical)[u'items'][i][u'track'][u'uri'])

uriCountry = 'spotify:user:spotify:playlist:37i9dQZF1DWYV2Gh2QglGo'
playlist_country = uriCountry.split(':')[4]
lengthCountry = sp.user_playlist_tracks('spotify', playlist_country)[u'items']
songsCountry = []
for i in range(len(lengthCountry)):
    songsCountry.append(sp.user_playlist_tracks('spotify', playlist_country)[u'items'][i][u'track'][u'uri'])

uriEdm = 'spotify:user:spotify:playlist:37i9dQZF1DX8tZsk68tuDw'
playlist_edm = uriEdm.split(':')[4]
lengthEdm = sp.user_playlist_tracks('spotify', playlist_edm)[u'items']
songsEdm = []
for i in range(len(lengthEdm)):
    songsEdm.append(sp.user_playlist_tracks('spotify', playlist_edm)[u'items'][i][u'track'][u'uri'])

uriHiphop = 'spotify:user:spotify:playlist:37i9dQZF1DWY6tYEFs22tT'
playlist_hiphop = uriHiphop.split(':')[4]
lengthHiphop = sp.user_playlist_tracks('spotify', playlist_hiphop)[u'items']
songsHiphop = []
for i in range(len(lengthHiphop)):
    songsHiphop.append(sp.user_playlist_tracks('spotify', playlist_hiphop)[u'items'][i][u'track'][u'uri'])

uriPop = 'spotify:user:spotify:playlist:37i9dQZF1DXarRysLJmuju'
playlist_pop = uriPop.split(':')[4]
lengthPop = sp.user_playlist_tracks('spotify', playlist_pop)[u'items']
songsPop = []
for i in range(len(lengthPop)):
    songsPop.append(sp.user_playlist_tracks('spotify', playlist_pop)[u'items'][i][u'track'][u'uri'])

uriRock = 'spotify:user:spotify:playlist:37i9dQZF1DXec50AjHrNTq'
playlist_rock = uriRock.split(':')[4]
lengthRock = sp.user_playlist_tracks('spotify', playlist_rock)[u'items']
songsRock = []
for i in range(len(lengthRock)):
    songsRock.append(sp.user_playlist_tracks('spotify', playlist_rock)[u'items'][i][u'track'][u'uri'])

uriRomance = 'spotify:user:spotify:playlist:37i9dQZF1DX5IDTimEWoTd'
playlist_romance = uriRomance.split(':')[4]
lengthRomance = sp.user_playlist_tracks('spotify', playlist_romance)[u'items']
songsRomance = []
for i in range(len(lengthRomance)):
    songsRomance.append(sp.user_playlist_tracks('spotify', playlist_romance)[u'items'][i][u'track'][u'uri'])


def findSong(case):
    #blues
    if (case==0):
        r = random.randint(0, len(songsBlues) - 1)
        print(r)
        song = []
        song.append(songsBlues[r])

    #chill
    elif(case==1):
        r = random.randint(0, len(songsChill) - 1)
        print(r)
        song = []
        song.append(songsChill[r])

    #classical
    elif(case==2):
        r = random.randint(0, len(songsClassical) - 1)
        print(r)
        song = []
        song.append(songsClassical[r])

    #country
    elif(case==3):
        r = random.randint(0, len(songsCountry) - 1)
        print(r)
        song = []
        song.append(songsCountry[r])

    #electronic/dance
    elif(case==4):
        r = random.randint(0, len(songsEdm) - 1)
        print(r)
        song = []
        song.append(songsEdm[r])

    #hip-hop
    elif(case==5):
        r = random.randint(0, len(songsHiphop) - 1)
        print(r)
        song = []
        song.append(songsHiphop[r])

    #pop
    elif(case==6):

        r = random.randint(0, len(songsPop) - 1)
        print(r)
        song = []
        song.append(songsPop[r])

    #rock
    elif(case==7):
        r = random.randint(0, len(songsRock) - 1)
        print(r)
        song = []
        song.append(songsRock[r])

    #romance
    elif(case==8):
        #uriTest = 'spotify:user:22twkvspkih7nwqom5dlty3hi:playlist:7yBfj4J84zawKqvqbDTVGc'
        r = random.randint(0, len(songsRomance)-1)
        print(r)
        song=[]
        song.append(songsRomance[r])
    return song

temp1=findSong(case)
addSong(temp1)
addSong(findSong(muse.get_curr_song_type())

while True:
    temp2 = findSong(muse.get_curr_song_type())
    if temp1!=temp2:
        #if sp.tracks(sp.user_playlist_tracks(username, playlist_id2)[u'items'][len(sp.user_playlist_tracks(username, playlist_id2)[u'items'])-1][u'track'][u'uri'])[0] == sp.currently_playing() :
        addSong(temp2)
        #else:
            #addNext(temp2)
    temp1=temp2
    time.sleep(10)
