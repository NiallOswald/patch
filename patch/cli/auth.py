"""Authentication commands."""

import typer

app = typer.Typer()


@app.command()
def status():
    """Check the current authentication status."""
    raise NotImplementedError


@app.command()
def login(username: str, password: str):
    """Log in to the server."""
    raise NotImplementedError


@app.command()
def logout():
    """Log out of patch."""
    raise NotImplementedError


@app.command()
def register(username: str, password: str):
    """Register a new account."""
    raise NotImplementedError


if __name__ == "__main__":
    app()
