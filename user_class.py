from playlist import Playlist
from songs_list import SongsList
import hashlib


class User:
    def __init__ (self,name,password,from_file):
        self.password = self.parse_password(password)

        if from_file:
            self.password=password
        self.name = name
        self.friends=[]
        self.playlists = {}

    def parse_password (self,password):
        return hashlib.md5(password.encode()).hexdigest()

    def change_password (self, old_password,new_password):
        if self.parse_password(old_password) == self.password:
            self.password = self.parse_password (new_password)
            return True
        else:
            return None

    def add_friend (self,friend_name):
        if friend_name in self.friends:
            return None
        else:
            self.friends.append (friend_name)
            return friend_name

    def add_playlist (self,playlist_name):
        if playlist_name in self.playlists.keys():
            return None
        
        self.playlists[playlist_name]=Playlist(playlist_name)
        return playlist_name
    

    def add_song_to_playlist (self,playlist_name,song_title):
        playlist = self.get_playlist(playlist_name)

        if playlist is None:
            return None
            
        if song_title not in playlist.get_songs():
            res = playlist.add_song(song_title)
            return res
        
        return None

    def get_playlist (self, playlist_name):
        try:
            return self.playlists[playlist_name]
        except KeyError:
            return None

    def get_details(self):
        return {
            "user_name":self.name,
            "playlists":list(self.playlists.keys()),
            "friends":self.friends
        }

    
