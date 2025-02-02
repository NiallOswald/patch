"""Tutorial for Cope-Pilot CLI."""

import typer

from time import sleep

import cope
from cope.utils import line_scroll


BANNER = r"""
 ______   ______   ______   ______             ______   ________  __       ______   _________  
/_____/\ /_____/\ /_____/\ /_____/\           /_____/\ /_______/\/_/\     /_____/\ /________/\ 
\:::__\/ \:::_ \ \\:::_ \ \\::::_\/_   _______\:::_ \ \\__.::._\/\:\ \    \:::_ \ \\__.::.__\/ 
 \:\ \  __\:\ \ \ \\:(_) \ \\:\/___/\ /______/\\:(_) \ \  \::\ \  \:\ \    \:\ \ \ \  \::\ \   
  \:\ \/_/\\:\ \ \ \\: ___\/ \::___\/_\__::::\/ \: ___\/  _\::\ \__\:\ \____\:\ \ \ \  \::\ \  
   \:\_\ \ \\:\_\ \ \\ \ \    \:\____/\          \ \ \   /__\::\__/\\:\/___/\\:\_\ \ \  \::\ \ 
    \_____\/ \_____\/ \_\/     \_____\/           \_\/   \________\/ \_____\/ \_____\/   \__\/
"""

PRE_TUTORIAL = [
    "We've all been there... you've been set a coding challenge, you've got a deadline, and you're stuck.",
    "You've tried everything you can think of, but you just can't get it to work.",
    "You have one place left to turn... ChatGPT.",
    "You enter in your problem, it spits out an answer, and you're done...",
    "...or so you think.",
    "Panic sets in! What do you do now?",
    "In Cope-Pilot, you are set an endless stream of challenges to complete.",
    "ChatGPT has tried and failed to pass the tests, your task is to debug.",
    "Let's get started!",
]

TUTORIAL = [
    "Use the command 'cope push' when you think you're done. Remember, it's all about speed, so push as many times as you need."
]

app = typer.Typer()


def push():
    """Submit the current problem for testing."""
    pass


@app.callback(invoke_without_command=True)
def main():
    # Display the banner
    print(BANNER)
    sleep(2)

    # Start the tutorial
    line_scroll(PRE_TUTORIAL)

    # Pull tutorial
    cope.start("tutorial")

    line_scroll(TUTORIAL)


if __name__ == "__main__":
    app()
