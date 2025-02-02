import typer

import datetime
import glob
import os
import random
import shutil

import problems

from pathlib import Path

from cope.config import Timer, Problem, Score, NullTimer
from cope.utils import clear_line

TRIAL_LENGTH = 5


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


def pull(problem_id: str = None):
    """Pull a new problem into the working directory."""
    typer.echo("… Pulling new problem")

    # Select a random problem
    if problem_id is None:
        problem_list = list(glob.glob(f"{problems.PATH}/*"))

        problem_list.remove(str(problems.PATH / "__init__.py"))

        # Do not randomly select tutorial
        problem_list.remove(str(problems.PATH / "tutorial"))
        try:
            problem_list.remove(str(problems.PATH / "__pycache__"))
        except ValueError:
            pass

        src_path = Path(random.choice(problem_list))

        problem_id = src_path.stem

    else:
        src_path = problems.PATH / problem_id

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
