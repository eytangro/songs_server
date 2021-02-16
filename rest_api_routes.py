from flask import jsonify, abort, request, Blueprint
import connexion
from flask import request
from flask.views import MethodView

REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


def add_user():
    print(connexion.request.json['user_name'])
    return 'Hello {name}'.format(name=connexion.request.json['user_name'])


def get_user():
    return 'Hello {name}'.format(name=connexion.request.args['user_name'])


def add_friend():
    return True


def change_password():
    return True


def add_playlist():
    return True


def add_song():
    return True


def song_upvote():
    return True


def song_downvote():
    return True


def ranked_songs():
    return True


def playlist_add_song():
    return True


def delete_all_users():
    return True


def delete_all_songs():
    return True


def set_songs():
    return True


def set_users():
    return True
