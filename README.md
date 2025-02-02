# CopePilot

A CLI game to train programmers in debugging AI-written solutions to LeetCode-style problems.
Points can be scored by completing randomised challenges, which are fed into GPT01 to provide a funcitoning, but not perfect solution to the problem. You then have a limited amount of time to find the bugs, squash them and pass all the tests! The points you score from the challenges will be added to a global leaderboard so you can compete with hackers in your back garden and around the world!

## Features

### Authorising users

### Leaderboard tracking

### A meta development and testing environemnt

### A rich and intuitive CLI for the game

### Integration with GPT01

### The invaluable ability to look critically at the output of LLMs

## Setup

For the program, we use a redis database for the leaderboard, a FastAPI backend for processing requests, and a stateless frontend CLI.

To set the program up, you can:

- Run the redis db (possibly in a docker container)
  e.g.

```
docker run -p 6379:6379 -it redis/redis-stack:latest
```

- Launch the FastAPI backend
  e.g. inside `/server`

```
fastapi dev main.py
```

- Install the `cope` package for the CLI
  e.g. in editable mode

```
python -m pip install -e .
```

## Playing!

Run, from any terminal any of the `cope` commands to begin!

You will find the following two very useful :)

```
cope tutorial
```

```
cope --help
```

Happing coping!
