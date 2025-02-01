To set up the server, we want:

- A Docker container running redis

```
docker run -p 6379:6379 -it redis/redis-stack:latest
```

- The FastAPI server

Run this in the `/server` directory.

```
fastapi dev main.py
```

Access at:

- http://127.0.0.1:8000/docs

Send requests to:

- http://127.0.0.1:8000/
