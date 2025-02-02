"""Main entry point for the cope CLI."""

import typer

from cope.cli import auth, highscore, leaderboard, timetrial

app = typer.Typer()
app.add_typer(auth.app, name="auth")
app.add_typer(timetrial.app, name="timetrial")
app.add_typer(highscore.app, name="highscore")
app.add_typer(leaderboard.app, name="leaderboard")

if __name__ == "__main__":
    app()
