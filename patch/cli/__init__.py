"""Main entry point for the patch CLI."""

import typer

from patch.cli import auth, timetrial, timer

app = typer.Typer()
app.add_typer(auth.app, name="auth")
app.add_typer(timetrial.app, name="timetrial")
app.add_typer(timer.app, name="timer")

if __name__ == "__main__":
    app()
