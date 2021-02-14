from songs_list import SongsList

class Playlist:
    def __init__(self, playlist_name):
        self.name = playlist_name
        self.songs = []

    
    def add_song (self,song_title):
        if song_title in self.get_songs():
            return None
        
        song = SongsList.get_song (song_title)

        if song is None:
            return None
    
        else:
            self.songs.append (song)
            return song_title
    
    def get_songs(self):
        return list(map(lambda x:x.title,self.songs))

    
    def delete_song (self,song_title):
        try:
            self.songs.remove (song_title)
            return song_title
        except ValueError:
            return None


    