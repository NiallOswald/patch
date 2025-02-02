"""Main entry point for the cope CLI."""

import typer

from pathlib import Path

import cope
from cope.cli import auth, highscore, leaderboard, tutorial

TRIAL_LENGTH = 5

app = typer.Typer()

app = typer.Typer()
app.add_typer(auth.app, name="auth", help="Register and log in.")
app.add_typer(tutorial.app, name="tutorial")
app.add_typer(highscore.app, name="highscore")
app.add_typer(leaderboard.app, name="leaderboard")


@app.command()
def status():
    """Check the current time trial status"""
    return cope.status()


@app.command()
def start():
    """Start a new time trial."""
    cope.start()


@app.command()
def quit():
    """Quit the current time trial."""
    cope.quit()


@app.command()
def push():
    """Submit the current problem for testing."""
    cope.push()


@app.command()
def skip():
    """Skip the current problem."""
    cope.skip()

if __name__ == "__main__":
    app()
