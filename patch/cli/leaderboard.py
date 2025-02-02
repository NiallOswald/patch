"""Leaderboard commands."""

import typer

from patch.utils import ur

app = typer.Typer()


@app.callback(invoke_without_command=True)
def leaderboard():
    """Show the highscores."""
    response = ur.leaderboard()
    if not ur.has_error(response):
        print(response.json())


if __name__ == "__main__":
    app()
