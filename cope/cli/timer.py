"""Time trial timer commands."""

import typer

from cope.cli import quit
from time import sleep


app = typer.Typer()


@app.command()
def start(length: int):
    """Start the time trial timer."""
    sleep(length)
    quit()


if __name__ == "__main__":
    app()
