"""Highscore commands."""

import typer

from cope.utils import ur

app = typer.Typer()


@app.callback(invoke_without_command=True)
def highscore():
    """Show the user's highscore."""
    response = ur.score()
    if not ur.has_error(response):
        print(response.json())


@app.command()
def top():
    """Show the highscores."""
    response = ur.leaderboard()
    if not ur.has_error(response):
        print(response.json())


if __name__ == "__main__":
    app()
