"""Time trial commands."""

import typer

app = typer.Typer()


@app.command()
def status():
    """Check the current time trial status."""
    raise NotImplementedError


@app.command()
def start():
    """Start a new time trial."""
    raise NotImplementedError


@app.command()
def quit():
    """Quit the current time trial."""
    raise NotImplementedError


@app.command()
def push():
    """Submit the current problem for testing."""
    raise NotImplementedError


@app.command()
def skip():
    """Skip the current problem."""
    raise NotImplementedError


if __name__ == "__main__":
    app()
