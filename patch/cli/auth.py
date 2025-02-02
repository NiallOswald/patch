"""Authentication commands."""

import typer

from patch.config import User, URL
from patch.utils import clear_line, ur

app = typer.Typer()


@app.command()
def status():
    """Check the current authentication status."""
    status = not ur.has_error(ur.status())

    if status:
        message = (
            typer.style("✓", fg=typer.colors.GREEN)
            + f" Logged in to patch leaderboard server account {User.get()["username"]}"
        )
    else:
        message = (
            typer.style("✗", fg=typer.colors.RED)
            + " Not logged in to patch leaderboard server account"
        )

    typer.echo(message, err=(not status))


@app.command()
def login(username: str, password: str):
    """Log in to the server."""
    User.set(username, password)
    ur.update_credentials(username, password)

    status = not ur.has_error(ur.status())

    if status:
        message = (
            typer.style("✓", fg=typer.colors.GREEN)
            + f" Logged in to patch leaderboard server account {username}"
        )
    else:
        message = typer.style("✗", fg=typer.colors.RED) + " Authentication failed"

    typer.echo(message, err=(not status))


@app.command()
def logout():
    """Log out of patch."""
    User.clear()
    typer.echo("Logged out of patch leaderboard server")


@app.command()
def register(username: str, password: str):
    """Register a new account."""
    # Register the user
    typer.echo("… Registering with patch leaderboard server")
    User.set(username, password)
    ur.update_credentials(username, password)
    reg_status = not ur.has_error(ur.sign_up())

    if reg_status:
        message = (
            typer.style("✓", fg=typer.colors.GREEN)
            + f" Registered with patch leaderboard server account {username}"
        )
    else:
        message = typer.style("✗", fg=typer.colors.RED) + " Registration failed"

    clear_line()
    typer.echo(message)

    # Test the authentication
    typer.echo("… Testing authentication")
    auth_status = not ur.has_error(ur.status())

    if auth_status:
        message = typer.style("✓", fg=typer.colors.GREEN) + " Authentication successful"
    else:
        message = typer.style("✗", fg=typer.colors.RED) + " Authentication failed"

    clear_line()
    typer.echo(message)

    # Final message
    if reg_status and auth_status:
        typer.echo("Registration complete")
    else:
        typer.echo("Registration failed", err=True)


@app.command()
def set_upstream(url: str):
    """Set the upstream server URL."""
    URL.set(url)
    typer.echo(f"Upstream server URL set to {url}")


if __name__ == "__main__":
    app()
