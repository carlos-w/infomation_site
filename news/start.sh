#!/bin/bash

export FLASK_DEBUG=1 
export FLASK_APP=app.py

flask run --port 3000 >flask.log 2>&1 &
