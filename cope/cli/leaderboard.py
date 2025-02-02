"""Leaderboard commands."""

import typer
from tabulate import tabulate

from cope.utils import ur

app = typer.Typer()


@app.callback(invoke_without_command=True)
def leaderboard():
    """Show the highscores."""
    response = ur.leaderboard()
    if not ur.has_error(response):
        data = response.json()
        headers = ["Username", "High Score"]
        print(tabulate(data.items(), headers=headers))


if __name__ == "__main__":
    app()
