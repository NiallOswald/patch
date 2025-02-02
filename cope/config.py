"""Module to manage the configuration file."""

import configparser
from pathlib import Path

config_path = Path.home() / "coperc.conf"

NullUser = {"username": None, "password": None}
NullTimer = {"init_time": None, "pid": None}
NullProblem = {"id": None, "path": None}
NullScore = {"score": None}


class Config:
    """Class to manage the configuration file."""

    @staticmethod
    def get() -> configparser.ConfigParser:
        """Load the configuration."""
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(config_path)
        return config

    @staticmethod
    def set(config: configparser.ConfigParser):
        """Save the configuration."""
        with open(config_path, "w") as f:
            config.write(f)


class User:
    """Class to manage the user credentials in the config file."""

    @staticmethod
    def get():
        """Return the user credentials from the config file."""
        config = Config.get()
        try:
            return config["user"]
        except KeyError:
            return dict()

    @staticmethod
    def set(username: str, password: str):
        """Set the user credentials in the config file."""
        config = Config.get()
        config["user"] = {"username": username, "password": password}
        Config.set(config)

    @staticmethod
    def clear():
        """Clear the user credentials in the config file."""
        config = Config.get()
        config["user"] = NullUser
        Config.set(config)


class Problem:
    """Class to manage the problem id and path in the config file."""

    @staticmethod
    def get():
        """Return the problem id and path from the config file."""
        config = Config.get()
        return config["problem"]

    @staticmethod
    def set(id: str, path: Path):
        """Set the problem id and path in the config file."""
        config = Config.get()
        config["problem"] = {"id": id, "path": path}
        Config.set(config)

    @staticmethod
    def clear():
        """Clear the problem id and path in the config file."""
        config = Config.get()
        config["problem"] = NullProblem
        Config.set(config)


class URL:
    """Class to manage the server URL in the config file."""

    @staticmethod
    def get():
        """Return the server URL from the config file."""
        config = Config.get()
        try:
            return config["server"]["url"]
        except KeyError:
            return dict()

    @staticmethod
    def set(url: str):
        """Set the server URL in the config file."""
        config = Config.get()
        config["server"] = {"URL": url}
        Config.set(config)


class Timer:
    """Class to manage the timer in the config file."""

    @staticmethod
    def get():
        """Return the timer from the config file."""
        config = Config.get()
        try:
            return config["timer"]
        except KeyError:
            return NullTimer

    @staticmethod
    def set(init_time: int, pid: int):
        """Set the timer in the config file."""
        config = Config.get()
        config["timer"] = {"init_time": init_time, "pid": pid}
        Config.set(config)

    @staticmethod
    def clear():
        """Clear the timer in the config file."""
        config = Config.get()
        config["timer"] = NullTimer
        Config.set(config)


class Score:
    """Class to manage the user score in the config file."""

    @staticmethod
    def get():
        """Return the user score from the config file."""
        config = Config.get()
        return config["score"]["score"]

    @staticmethod
    def set(score: int):
        """Set the user score in the config file."""
        config = Config.get()
        config["score"] = {"score": score}
        Config.set(config)

    @staticmethod
    def clear():
        """Clear the user score in the config file."""
        config = Config.get()
        config["score"] = NullScore
        Config.set(config)
