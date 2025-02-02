"""Utility functions for the CLI."""

import sys
from importlib.util import spec_from_file_location, module_from_spec
from time import sleep

from cope.config import User, URL
from server.rest import UserRequests

LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"

ur = UserRequests(**URL.get(), **User.get())


def clear_line(n=1):
    """Clear the current line."""
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


def import_from_path(path, module_name: str):
    """Import a module from a file path."""
    spec = spec_from_file_location(module_name, path)
    module = module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


def line_scroll(str_list):
    for line in str_list:
        for i in range(len(line)):
            print(line[: i + 1], end="\r")
            sleep(0.1)
        sleep(1)
        print()
        print()
