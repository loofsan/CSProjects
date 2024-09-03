import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = '316w4jcn4ie5wr7du4fr63qg7u3e'

token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

#create the playlist
playlist_name = "School Playlist"
playlist_description = "School Playlist"

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)


list_of_songs = []
file1 = open("C:\Lynn\Python\spotifyPlaylist\playlist.txt", 'r')
Lines = file1.readlines()

#Grab from list
for line in Lines:
    result = spotifyObject.search(q=line)
    #print(json.dumps(result,sort_keys=4,indent=4))
    list_of_songs.append(result['tracks']['items'][0]['uri'])

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#Add songs
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)