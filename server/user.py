HASHED_PASSWORD = "hashed_password"
SCORE = "score"


class User:

    def __init__(self, username: str, hashed_password: str, score: int = 0):
        self.username = username
        self.hashed_password = hashed_password
        self.score = score

    def __set_score(self, score: int):
        self.score = score

    def update_highscore(self, new_score: int):
        if new_score > self.score:
            self.__set_score(new_score)

    def get_db_object_mapping(self):
        return {HASHED_PASSWORD: self.hashed_password, SCORE: self.score}

    @classmethod
    def from_db_object_mapping(self, username: str, mapping: dict):
        return User(
            username,
            mapping.get(str.encode(HASHED_PASSWORD)).decode(),
            int(mapping.get(str.encode(SCORE)).decode()),
        )

    def __str__(self):
        return f"User({self.username}, {self.hashed_password}, {self.score})"
