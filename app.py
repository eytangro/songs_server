# from playlist_list import Playlist_list
from playlist import Playlist
from song_class import Song
from songs_list import SongsList
from user_class import User
from users import Users
import set_from_db

def main():
    set_from_db.get_songs_from_file()
    set_from_db.get_users_from_file()
    # Users.initiate_users()
    # SongsList.initiate_songs()
    Users.add_user ("eytan","123")

    e = Users.get_user ("eytan")

    e.change_password ("123","456")

    e.add_playlist ("lala")
    e.add_playlist ("lala2")

    p = e.get_playlist ("lala")
  
    s1 = Song ("hamilton",2010,"rap","lin manuel miranda")
    s2= Song ("hamilton_1",2010,"rap","lin manuel miranda")
    SongsList.add_song (s1)
    SongsList.add_song (s2)
    e.add_song_to_playlist ("lala","hamilton")
    e.add_song_to_playlist ("lala","hamilton_1")
    e.add_song_to_playlist ("lala2","hamilton_1")
    

    set_from_db.write_users_to_file()
    set_from_db.write_songs_to_file()
    print("h")




if __name__ == "__main__":
    main()
