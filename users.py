from user_class import User


class Users:

    @classmethod
    def initiate_users(cls):
        cls.users = {}

    @classmethod
    def add_user(cls, user_name, user_password,from_file = False):
        if user_name not in cls.users.keys():
            cls.users[user_name] = User(user_name, user_password,from_file)
            return user_name

        return None

    @classmethod
    def get_user(cls, user_name):
        try:
            return cls.users[user_name]
        except KeyError:
            return None


    @classmethod
    def add_playlist_to_user (cls,user_name, playlist_name):
        user = cls.get_user (user_name)

        if user is not None:
            user.add_playlist (playlist_name)
            return playlist_name
        

        return None


    @classmethod
    def delete_user (cls,user_name):
        cls.users.pop (user_name,None)
        return True
