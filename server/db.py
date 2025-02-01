import redis
from server.user import User


class Database:

    def __init__(self, host="localhost", port="6379"):
        self.db = redis.Redis(host=host, port=port, db=0)

    def __put_user(self, user: User):
        self.db.hset(user.username, mapping=user.get_db_object_mapping())

    def __get_user(self, username: str) -> User:
        return self.db.hgetall(username)

    def __user_exists(self, username: str):
        return self.db.exists(username) > 0

    def create_user(self, username: str, hashed_password: str):
        if not self.__user_exists(username):
            user = User(username, hashed_password)
            self.__put_user(user)
            return True
        else:
            return False

    def retrieve_user(self, username: str) -> User:
        if self.__user_exists(username):
            return User.from_db_object_mapping(username, self.__get_user(username))
        else:
            return None

    def update_highscore(self, username: str, score: int):
        user = self.retrieve_user(username)
        if user is None:
            return False

        user.update_highscore(score)

        self.__put_user(user)
        return True

    def authenticate(self, username, hashed_password) -> bool:
        """
        Attempt to authenticate with the specified username.
        If the username does not exist, will return False.
        If the username exists and the password does not match, will return False.
        Otherwise, will return True.
        """
        user = self.retrieve_user(username)
        if user is None:
            return False

        return hashed_password == user.hashed_password

    def retrieve_all_users(self):
        """
        Retrieve all users.
        """
        scores = {}
        for encoded_name in self.db.scan_iter():
            print(encoded_name)
            name = encoded_name.decode()
            scores[name] = self.retrieve_user(name).score
        print(scores)
        return scores
