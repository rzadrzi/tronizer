#!/bin/bash

HOST=127.0.0.1
PORT=8000
source venv/bin/activate
uvicorn app.main:app --host $HOST --port $PORT --lifespan on --reload

#uvicorn app.main:app --host 128.0.0.1 --port 8000
