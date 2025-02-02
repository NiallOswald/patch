from server.constants import SCORE, PASSWORD


class User:

    def __init__(self, username: str, password: str, score: int = 0):
        self.username = username
        self.password = password
        self.score = score

    def __set_score(self, score: int):
        self.score = score

    def update_highscore(self, new_score: int):
        if new_score > self.score:
            self.__set_score(new_score)

    def get_db_object_mapping(self):
        return {PASSWORD: self.password, SCORE: self.score}

    @classmethod
    def from_db_object_mapping(cls, username: str, mapping: dict):
        return cls(
            username,
            mapping.get(str.encode(PASSWORD)).decode(),
            int(mapping.get(str.encode(SCORE)).decode()),
        )

    def __str__(self):
        return f"User({self.username}, {self.password}, {self.score})"
