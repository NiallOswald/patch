"""Time trial timer."""

from argparse import ArgumentParser
from patch.cli.timetrial import quit
from time import sleep


def start(length: int):
    """Start the time trial timer."""
    sleep(length)
    quit()


def main():
    parser = ArgumentParser(description="Time trial timer.")
    parser.add_argument("length", type=int, help="Length of the time trial in seconds.")
    args = parser.parse_args()
    start(args.length)
