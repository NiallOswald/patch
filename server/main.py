from fastapi import FastAPI, HTTPException
from server.db import Database
from server.paths import AUTH_SIGN_UP, AUTH_STATUS, LEADERBOARD, SCORE, TIMETRIAL

app = FastAPI()
db = Database()


@app.post(AUTH_SIGN_UP)
def sign_up(username: str, hashed_password: str):
    """
    Attempt to store new user in the database. Returns 200 OK if no problem.
    Return appropriate error codes if duplicate or incorrect types. Error out for multiple! (Don't overwrite)
    """
    if db.create_user(username, hashed_password):
        return True
    else:
        raise HTTPException(status_code=400, detail="User exists already")


@app.post(AUTH_STATUS)
def status(username: str, hashed_password: str):
    """
    Attempt to check validity of credentials. Returns 200 OK if no problem.
    Returns appropriate error codes if user doesn't exist or incorrect types/values
    """
    if db.authenticate(username, hashed_password):
        return True
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")


@app.get(LEADERBOARD)
def leaderboard():
    """
    Return current leaderboard data.
    """
    return db.retrieve_all_users()


@app.get(SCORE)
def score(username: str, hashed_password: str):
    """
    Return your highscore. (And auth)
    """
    if not db.authenticate(username, hashed_password):
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db.retrieve_user(username).score


@app.post(TIMETRIAL)
def timetrial(username: str, hashed_password: str, score: int):
    """
    Submit a result and replace the highscore if higher (And auth)
    """
    if not db.authenticate(username, hashed_password):
        raise HTTPException(status_code=401, detail="Authentication failed")
    db.update_highscore(username, score)
    return True
