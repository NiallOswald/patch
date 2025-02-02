"""Main entry point for the cope CLI."""

import typer

import datetime
import glob
import os
import random
import shutil
import signal
import subprocess

from pathlib import Path

import problems

from cope.cli import auth, highscore, leaderboard
from cope.config import Score, Timer, Problem, NullTimer, User
from cope.utils import ur, clear_line, import_from_path

TRIAL_LENGTH = 5

app = typer.Typer()

app = typer.Typer()
app.add_typer(auth.app, name="auth", help="Register and log in.")
app.add_typer(highscore.app, name="highscore")
app.add_typer(leaderboard.app, name="leaderboard")


@app.command()
def status():
    """Check the current time trial status."""
    timer = Timer.get()

    if dict(timer) == NullTimer:
        message = typer.style("✗", fg=typer.colors.RED) + " No time trial in progress"
        typer.echo(message)

        return

    elapsed_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        int(timer["init_time"])
    )
    time_remaining = datetime.timedelta(minutes=TRIAL_LENGTH) - elapsed_time

    score = Score.get()
    typer.echo(
        f"Time remaining: {str(time_remaining)[2:-4]} Score: {score}"
    )  # Messy but works


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


def pull():
    """Pull a new problem into the working directory."""
    typer.echo("… Pulling new problem")

    # Select a random problem
    problem_list = list(glob.glob(f"{problems.PATH}/*"))

    problem_list.remove(str(problems.PATH / "__init__.py"))
    try:
        problem_list.remove(str(problems.PATH / "__pycache__"))
    except ValueError:
        pass

    src_path = Path(random.choice(problem_list))

    problem_id = src_path.stem

    # Copy the problem to the working directory
    working_dir = Path.cwd()
    shutil.copytree(src_path, working_dir / src_path.stem)

    # Save problem to config
    Problem.set(problem_id, working_dir / src_path.stem)

    message = typer.style("✓", fg=typer.colors.GREEN) + " Problem pulled successfully"
    clear_line()
    typer.echo(message)

    # Show status
    status()


def cleanup():
    """Clean up the working directory."""
    typer.echo("… Cleaning up working directory")

    # Remove all files in the working directory
    problem = Problem.get()
    dir_path = Path(problem["path"])

    for filename in ["task.md", "skeleton.py", "test.py"]:
        try:
            os.remove(dir_path / filename)
        except FileNotFoundError:
            pass

    # Deal with pycache
    try:
        shutil.rmtree(dir_path / "__pycache__")
    except FileNotFoundError:
        pass

    os.rmdir(dir_path)

    # Clear problem from config
    Problem.clear()

    message = typer.style("✓", fg=typer.colors.GREEN) + " Clean-up complete"
    clear_line()
    typer.echo(message)


if __name__ == "__main__":
    app()
