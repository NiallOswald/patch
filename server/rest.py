import requests
from server.paths import AUTH_SIGN_UP, AUTH_STATUS, LEADERBOARD, SCORE, TIMETRIAL
from server.constants import PASSWORD, USERNAME, SCORE

BASE_URL = "http://127.0.0.1:8000/"


class UserRequests:

    def __init__(self, URL=BASE_URL, username: str = None, password: str = None):
        self.URL = URL
        self.update_credentials(username, password)

    def update_credentials(self, username: str, password: str):
        self.username = username
        self.password = password

    def sign_up(self):
        return requests.post(self.URL + AUTH_SIGN_UP, params=self.get_user_login_json())

    def status(self):
        return requests.post(self.URL + AUTH_STATUS, params=self.get_user_login_json())

    def leaderboard(self):
        return requests.get(self.URL + LEADERBOARD)

    def score(self):
        return requests.get(self.URL + SCORE, params=self.get_user_login_json())

    def timetrial(self, score: int):
        data = self.get_user_login_json()
        data[SCORE] = score
        return requests.post(self.URL + TIMETRIAL, params=data)

    def get_user_login_json(self):
        return {USERNAME: self.username, PASSWORD: self.password}

    @classmethod
    def has_error(cls, response: requests.Response):
        return response.status_code != 200

    @classmethod
    def get_error_detail(cls, response: requests.Response):
        """
        Get the error message, assuming there is an error (i.e. not a 200 OK status code)
        """
        return response.json().get("detail")
