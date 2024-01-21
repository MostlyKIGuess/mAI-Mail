make ingest ./data -- --watch

#inside new terminal
source .venv/bin/activate
# Launch the privateGPT API server **and** the gradio UI
poetry run python3.11 -m private_gpt
# In another terminal, create a new browser window on your private GPT!
open http://127.0.0.1:8001/




make wipe