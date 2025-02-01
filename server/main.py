from fastapi import FastAPI

app = FastAPI()


@app.post("/auth/sign_up")
def sign_up(username: str, hashed_password: str):
    """
    Attempts to store new user in the database. Returns 200 OK if no problem.
    Returns appropriate error codes if duplicate or incorrect types. Error out for multiple! (Don't overwrite)
    """


@app.post("/auth/status")
def login(username: str, hashed_password: str):
    """
    Attempts to check validity of credentials. Returns 200 OK if no problem.
    Returns appropriate error codes if user doesn't exist or incorrect types/ values
    """


@app.get("/leaderboard")
def leaderboard():
    """
    Returns current leaderboard data.
    """


@app.post("/score")
def score():
    """
    Returns your highscore. (And auth)
    """


@app.post("/timetrial")
def timetrial():
    """
    Submit a result and replace the highscore if higher (And auth)
    """
