class SongsList:

    @classmethod
    def initiate_songs (cls):
        cls.songs_list = {}


    @classmethod
    def get_song (cls,song_title):
        try:
            return cls.songs_list[song_title]
        except KeyError:
            return None

    @classmethod
    def add_song (cls,song):
        if song.title in cls.songs_list.keys():
            return None
        else:
            cls.songs_list[song.title] = song
            return song.title
    
    @classmethod
    def get_all_songs (cls):
        return list(cls.songs_list.keys())

    @classmethod
    def get_all_songs_obj (cls):
        return cls.songs_list