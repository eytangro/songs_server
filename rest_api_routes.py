import configparser
import connexion
import requests

config = configparser.ConfigParser()
config.read('./sources/config.ini')
host = config['target']['host']
port = config['target']['port']
target = 'http://' + host + ':' + port


def add_user():
    r = requests.post(url=target + '/users/add_user', json=connexion.request.json)
    print(r)
    return r.json()


def get_user():
    r = requests.get(url=target + '/users/get_user', params={'user_name': connexion.request.args['user_name']})
    print(connexion.request.args['user_name'])
    return r.json()


def add_friend():
    r = requests.put(url=target + '/users/add_friend', json=connexion.request.json)
    return r.json()


def change_password():
    r = requests.put(url=target + '/users/change_password', json=connexion.request.json)
    return r.json()


def add_playlist():
    r = requests.post(url=target + '/users/add_playlist', json=connexion.request.json)
    return r.json()


def add_song():
    r = requests.post(url=target + '/songs/add_song', json=connexion.request.json)
    return r.json()


def song_upvote():
    r = requests.put(url=target + '/songs/upvote', json=connexion.request.json)
    return r.json()


def song_downvote():
    r = requests.put(url=target + '/songs/downvote', json=connexion.request.json)
    return r.json()


def ranked_songs():
    payload = {'rank': connexion.request.args['rank'], 'op': connexion.request.args['op']}
    r = requests.get(url=target + '/songs/ranked_songs', params=payload)
    return r.json()


def playlist_add_song():
    r = requests.post(url=target + '/playlists/add_song', json=connexion.request.json)
    return r.json()


def delete_all_users():
    r = requests.delete(target + '/admin/delete_all_users')
    return r.json()


def delete_all_songs():
    r = requests.delete(target + '/admin/delete_all_songs')
    return r.json()


def set_songs():
    r = requests.post(url=target + '/admin/set_songs', json=connexion.request.json)
    return r.json()


def set_users():
    r = requests.post(url=target + '/admin/set_users', json=connexion.request.json)
    return r.json()
