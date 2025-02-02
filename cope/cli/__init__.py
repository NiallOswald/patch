"""Main entry point for the cope CLI."""

import typer

import datetime
import os
import signal
import subprocess

from pathlib import Path

from cope.cli import auth, highscore, leaderboard, tutorial
from cope.config import Score, Timer, Problem, NullTimer, User
from cope.utils import ur, clear_line, import_from_path
from cope import status as _status
from cope import cleanup, pull

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
    return _status()


@app.command()
def start():
    """Start a new time trial."""
    timer = Timer.get()

    # Can only start a time trial if one is not already in progress
    if timer != NullTimer:
        message = (
            typer.style("✗", fg=typer.colors.RED) + " Time trial already in progress"
        )
        typer.echo(message)

        return

    # Check auth
    status = not ur.has_error(ur.status())

    if status:
        message = (
            typer.style("✓", fg=typer.colors.GREEN)
            + f" Logged in to cope leaderboard server account {User.get()["username"]}, so your results will be uploaded."
        )
    else:
        message = (
            typer.style("✗", fg=typer.colors.RED)
            + " Not logged in to cope leaderboard server account, so results will not be uploaded.. You can quit, log in and restart to have your results uploaded."
        )

    typer.echo(message, err=(not status))

    # Reset score
    Score.set(0)

    # Start timer subprocess
    proc = subprocess.Popen(["cope-timer", str(TRIAL_LENGTH * 60)])

    # Save timer to config
    Timer.set(int(datetime.datetime.now().timestamp()), proc.pid)

    # Pull first problem
    pull()


@app.command()
def quit():
    """Quit the current time trial."""
    timer = Timer.get()

    # Can only quit a time trial if one is in progress
    if dict(timer) == NullTimer:
        message = typer.style("✗", fg=typer.colors.RED) + " No time trial in progress"
        typer.echo(message)

        return

    # Kill timer subprocess
    os.kill(int(timer["pid"]), signal.SIGTERM)

    # Clear timer from config
    Timer.clear()

    # Clean-up working directory
    cleanup()

    # Push results to leaderboard server
    score = Score.get()

    typer.echo("… Uploading results to cope leaderboard server")

    if ur.has_error(ur.status()):
        message = (
            typer.style("✗", fg=typer.colors.RED)
            + " Not logged in to cope leaderboard server"
        )

    elif ur.has_error(ur.timetrial(score)):
        message = (
            typer.style("✗", fg=typer.colors.RED)
            + " Post to cope leaderboard server failed"
        )

    else:
        message = (
            typer.style("✓", fg=typer.colors.GREEN)
            + " Posted score to cope leaderboard server successfully"
        )

    clear_line()
    typer.echo(message)

    # Clear score
    Score.clear()

    # Show results
    typer.echo(f"Final score: {score}")


@app.command()
def push():
    """Submit the current problem for testing."""
    timer = Timer.get()

    # Can only quit a time trial if one is in progress
    if dict(timer) == NullTimer:
        message = typer.style("✗", fg=typer.colors.RED) + " No time trial in progress"
        typer.echo(message)

        return

    problem = Problem.get()
    path = Path(problem["path"])

    # Load skeleton code
    skeleton = import_from_path(
        path / "skeleton.py", "skeleton"
    )  # Don't ever delete this, _ever_

    # Load test code
    test = import_from_path(path / "test.py", "test")

    # Run tests
    test.main()

    # Increment score
    Score.set(int(Score.get()) + 1)

    # Clean-up last problem
    cleanup()

    # Pull new problem
    pull()


@app.command()
def skip():
    """Skip the current problem."""
    typer.echo("… Skipping problem")

    # Clean-up last problem
    cleanup()

    message = typer.style("✓", fg=typer.colors.GREEN) + " Problem skipped"
    typer.echo(message)

    # Pull new problem
    pull()


if __name__ == "__main__":
    app()
