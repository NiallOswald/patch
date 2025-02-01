"""Module to manage the configuration file."""

import configparser
from pathlib import Path

config_path = Path.home() / "coperc.conf"


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
        return config["user"]

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
        config["user"] = {"username": None, "password": None}
        Config.set(config)


class Problem:
    """Class to manage the problem id and path in the config file."""

    @staticmethod
    def get_id():
        """Return the problem id from the config file."""
        config = Config.get()
        return config["problem_id"]

    @staticmethod
    def set_id(problem_id: str):
        """Set the problem id in the config file."""
        config = Config.get()
        config["problem_id"] = {"problem_id": problem_id}
        Config.set(config)

    @staticmethod
    def clear_id():
        """Clear the problem id in the config file."""
        config = Config.get()
        config["problem_id"] = {"problem_id": None}
        Config.set(config)

    @staticmethod
    def get_path():
        """Return the problem path from the config file."""
        config = Config.get()
        return Path(config["problem_path"])

    @staticmethod
    def set_path(problem_path: Path):
        """Set the problem path in the config file."""
        config = Config.get()
        config["problem_path"] = {"problem_path": problem_path}
        Config.set(config)

    @staticmethod
    def clear_path():
        """Clear the problem path in the config file."""
        config = Config.get()
        config["problem_path"] = {"problem_path": None}
        Config.set(config)
