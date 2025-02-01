"""Main entry point for the patch CLI."""

import typer

from patch.cli import auth, timetrial

app = typer.Typer()
app.add_typer(auth.app, name="auth")
app.add_typer(timetrial.app, name="timetrial")

if __name__ == "__main__":
    app()
