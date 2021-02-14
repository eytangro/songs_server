import json
from playlist import Playlist
from song_class import Song
from songs_list import SongsList
from user_class import User
from users import Users

songs_file_path = "songs.json"
users_file_path = "users.json"


def get_songs_from_file():
    try:
        with open(songs_file_path, 'r') as f:
            songs = json.load(f)
    except:
        songs = []

    get_songs_from_source (songs)


def get_songs_from_source (songs):
    SongsList.initiate_songs()

    for current in songs:
        song = Song(current['title'], current['year'],
                    current['genre'], current['performer'])
        song.rating = current['rating']
        SongsList.add_song(song)

def get_users_from_file():
    try:
        with open(users_file_path, 'r') as f:
            users = json.load(f)
    except:
        users = {}

    get_users_from_source (users)


def get_users_from_source (users):
    Users.initiate_users()
    for k, v in users.items():
        name = v['name']
        password = v['password']
        Users.add_user(name, password, True)
        user = Users.get_user(name)
        user.friends = v['friends']
        for playlist_name, songs in v['playlists'].items():
            user.add_playlist(playlist_name)
            for song in songs:
                user.add_song_to_playlist(playlist_name, song)


def write_songs_to_file():
    all_songs = []
    for s in SongsList.get_all_songs():
        song = SongsList.get_song(s)
        to_write = {
            "title": song.title,
            "year": song.year,
            "genre": song.genre,
            "performer": song.performer,
            "rating": song.rating
        }
        all_songs.append(to_write)

    with open(songs_file_path, 'w')as f:
        f.write(json.dumps(all_songs, indent=4))


def write_users_to_file():
    all_users = {}

    for k, v in Users.users.items():
        playlists = {}
        for play_name, values in v.playlists.items():
            playlist_songs = []
            for song in values.songs:
                playlist_songs.append(song.title)

            playlists[play_name] = playlist_songs

        user = {
            "password": v.password,
            "name": v.name,
            "friends": v.friends,
            "playlists": playlists
        }
        all_users[v.name] = user

    with open(users_file_path, 'w')as f:
        f.write(json.dumps(all_users, indent=4))
