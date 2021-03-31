from flask import Flask, jsonify
from flask import request
from playlist import Playlist
from song_class import Song
from songs_list import SongsList
from user_class import User
from users import Users
import validations
import set_from_db

app = Flask(__name__)


@app.route("/users/add_user", methods=['POST'])
def add_user():
    user_name = request.json.get("user_name")
    user_password = request.json.get("user_password")

    valid = validations.valid_parameters(
        user_name=user_name, user_password=user_password)
    if valid != True:
        return valid

    user = Users.add_user(user_name, user_password)

    if user is None:
        return {
            "error": f"user with name {user_name} already exists."
        }

    set_from_db.write_users_to_file()

    return {
        "messgae": "OK",
        "data": user
    }


@app.route("/users/get_user", methods=['GET'])
def get_user():
    user_name = request.args.get("user_name")
    valid = valid_parameters(user_name=user_name)

    if valid != True:
        return valid

    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"user {user_name} does not exist"
        }

    else:
        return {
            "message": "OK",
            "data": user.get_details()
        }



@app.route("/users/change_password", methods=['PUT'])
def change_user_password():
    user_name = request.json.get("user_name")
    user_password = request.json.get("user_password")
    user_new_password = request.json.get("user_new_password")
    valid = valid_parameters(user_name=user_name,user_password = user_password,user_new_password = user_new_password)

    if valid != True:
        return valid

    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"user {user_name} does not exist"
        }

    res = user.change_password (user_password,user_new_password)

    if res is None:
        return{
            "error":"some parameters are wrong"
        }

    else:
        set_from_db.write_users_to_file()

        return {
            "message": "OK",
            "data": user.get_details()
        }


@app.route("/songs/ranked_songs", methods=['GET'])
def get_ranked_songs():
    rank = int(request.args.get("rank"))
    op = request.args.get("op")

    valid = valid_parameters(rank=rank, op=op)

    if valid != True:
        return valid

    all_songs = SongsList.get_all_songs_obj()
    returned_songs = []
    if op == "less":
        returned_songs = [v.title for 
                          v in all_songs.values() if v.rating < rank]
    elif op == "eq":
        returned_songs = [v.title for 
                          v in all_songs.values() if v.rating == rank]
    elif op == "greater":
        returned_songs = [v.title for 
                          v in all_songs.values() if v.rating > rank]
    else:
        return {
            "error": f"no such operation {op}"
        }
    
    return {
        "message":"OK",
        "data":returned_songs
    }


@app.route("/users/add_friend", methods=['PUT'])
def add_friend():
    user_name = request.json.get("user_name")
    user_password = request.json.get("user_password")
    friend_name = request.json.get("friend_name")

    valid = valid_parameters(
        user_name=user_name, user_password=user_password, friend_name=friend_name)

    if valid != True:
        return valid

    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"the user {user_name} does not exist"
        }

    if user.password != user.parse_password(user_password):
        return {
            "error": f"either the user name or the password are wrong"
        }

    res = user.add_friend(friend_name)

    if res is None:
        return {
            "error": f"{friend_name} already a friend of {user_name}"
        }

    set_from_db.write_users_to_file()

    return {
        "message": "OK",
        "data": res
    }


@app.route("/users/add_playlist", methods=['POST'])
def add_playlist():
    user_name = request.json.get("user_name")
    user_password = request.json.get("user_password")
    playlist_name = request.json.get("playlist_name")

    valid = valid_parameters(
        user_name=user_name, user_password=user_password, playlist_name=playlist_name)

    if valid != True:
        return valid

    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"the user {user_name} does not exist"
        }

    if user.password != user.parse_password(user_password):
        return {
            "error": f"either the user name or the password are wrong"
        }

    res = user.add_playlist(playlist_name)

    if res is None:
        return {
            "error": f"{playlist_name} already a playlist of {user_name}"
        }

    set_from_db.write_users_to_file()

    return {
        "message": "OK",
        "data": res
    }


@app.route ("/users/get_playlist", methods=['GET'])
def get_playlist():
    user_name = request.args.get("user_name")
    user_password = request.args.get("user_password")
    playlist_name = request.args.get("playlist_name")

    valid = valid_parameters(
        user_name=user_name, user_password=user_password, playlist_name=playlist_name)

    if valid != True:
        return valid


    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"the user {user_name} does not exist"
        }

    if user.password != user.parse_password(user_password):
        return {
            "error": f"either the user name or the password are wrong"
        }

    playlist = user.get_songs_in_playlist (playlist_name)

    return {
        "message":"OK",
        "data":playlist
    }



@app.route("/songs/add_song", methods=["POST"])
def add_song():
    song_title = request.json.get("song_title")
    song_genre = request.json.get("song_genre")
    song_year = request.json.get("song_year")
    song_performer = request.json.get("song_performer")

    valid = valid_parameters(
        song_title=song_title, song_genre=song_genre, song_year=song_year, song_performer=song_performer)

    if valid != True:
        return valid

    s = Song(song_title, song_year, song_genre, song_performer)
    add_song = SongsList.add_song(s)

    if add_song is None:
        return {
            "error": "this song already exist in the collection"
        }

    set_from_db.write_songs_to_file()

    return {
        "message": "OK",
        "data": song_title
    }


@app.route ("/songs/get_song",methods = ['GET'])
def get_song ():
    song_title = request.args.get("song_title")

    valid = valid_parameters(song_title=song_title)

    if valid != True:
        return valid
    
    song = SongsList.get_song (song_title)

    if song is None:
        return {
            "error":"this song does not exsist"
        }

    return {
        "message":"OK",
        "data":song.get_details()
    }


@app.route("/playlists/add_song", methods=['POST'])
def add_song_to_playlist():
    user_name = request.json.get("user_name")
    user_password = request.json.get("user_password")
    playlist_name = request.json.get("playlist_name")
    song_title = request.json.get("song_title")

    valid = valid_parameters(
        user_name=user_name, user_password=user_password, playlist_name=playlist_name, song_title=song_title)

    if valid != True:
        return valid

    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"the user {user_name} does not exist"
        }

    if user.password != user.parse_password(user_password):
        return {
            "error": f"either the user name or the password are wrong"
        }

    res = user.add_song_to_playlist(playlist_name, song_title)

    if res is None:
        return {
            "error": f"the song {song_title} already exist in the playlist or not in the songs collection"
        }

    set_from_db.write_users_to_file()

    return {
        "message": "OK",
        "data": res
    }


@app.route("/songs/upvote", methods=['PUT'])
def upvote_song():
    user_name = request.json.get("user_name")
    user_password = request.json.get("user_password")
    song_title = request.json.get("song_title")

    valid = valid_parameters(
        user_name=user_name, user_password=user_password, song_title=song_title)

    if valid != True:
        return valid

    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"the user {user_name} does not exist"
        }

    if user.password != user.parse_password(user_password):
        return {
            "error": f"either the user name or the password are wrong"
        }

    s = SongsList.get_song(song_title)

    if s is None:
        return {
            "error": "no such song in the songs collection"
        }

    s.upvote()
    set_from_db.write_songs_to_file()

    return {
        "message": "OK",
        "data": {
            "song_title": song_title,
            "rating": s.rating
        }
    }


@app.route("/songs/downvote", methods=['PUT'])
def downvote_song():
    user_name = request.json.get("user_name")
    user_password = request.json.get("user_password")
    song_title = request.json.get("song_title")

    valid = valid_parameters(
        user_name=user_name, user_password=user_password, song_title=song_title)

    if valid != True:
        return valid

    user = Users.get_user(user_name)

    if user is None:
        return {
            "error": f"the user {user_name} does not exist"
        }

    if user.password != user.parse_password(user_password):
        return {
            "error": f"either the user name or the password are wrong"
        }

    s = SongsList.get_song(song_title)

    if s is None:
        return {
            "error": "no such song in the songs collection"
        }

    s.downvote()
    set_from_db.write_songs_to_file()

    return {
        "message": "OK",
        "data": {
            "song_title": song_title,
            "rating": s.rating
        }
    }


@app.route("/admin/delete_all_users", methods=['DELETE'])
def delete_all_users():
    Users.users = {}

    set_from_db.write_users_to_file()

    return {
        "message": "OK"
    }


@app.route("/admin/delete_all_songs", methods=['DELETE'])
def delete_all_songs():
    SongsList.songs_list = {}

    set_from_db.write_songs_to_file()

    return {
        "message": "OK"
    }


@app.route("/admin/set_users", methods=["POST"])
def set_users():
    users = request.json.get("users")

    set_from_db.get_users_from_source(users)

    set_from_db.write_users_to_file()

    return {
        "messgae": "OK"
    }


@app.route("/admin/set_songs", methods=['POST'])
def set_songs():
    songs = request.json.get("songs")

    set_from_db.get_songs_from_source(songs)

    set_from_db.write_songs_to_file()

    return {
        "messgae": "OK"
    }



@app.route ("/admin/delete_user",methods=["DELETE"])
def delete_user():
    user_name = request.json.get("user_name")

    Users.delete_user (user_name)
    set_from_db.write_users_to_file()


    return{
        "message":"OK"
    }



def valid_parameters(**kwargs):
    for key, value in kwargs.items():
        if value is None:
            return {
                "error": f"Misssing parameter {key}"
            }
    return True


def run_server():
    app.run(port=3002)


if __name__ == "__main__":
    set_from_db.get_songs_from_file()
    set_from_db.get_users_from_file()
    run_server()
