#!/bin/bash

python3 ./scrapper/pythongmail.py


bash ./scrapper/threadcopy.sh

# Start a new detached tmux session for the make command
tmux new-session -d -s my_session 'make ingest ./data -- --watch'

# Activate the virtual environment and start the private GPT API server in a new tmux window
tmux new-window -t my_session:1 'source .venv/bin/activate; poetry run python3.11 -m private_gpt'

# Open a new browser window on your private GPT in a new tmux window
tmux new-window -t my_session:2 'open http://127.0.0.1:8001/'

# Attach to the tmux session
tmux attach -t my_session