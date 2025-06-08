# accessLlamaModelOnHuggingFace
This project tests accessing a Llama model on Hugging Face using an API key, since there are multiple (confusing) steps for successful authentication.
A Windows CMD shell should not be used, since it does not support symbolic links, and will cause multiple copies of the very large (20GB) files to be downloaded.  Instead, use WSL (Windows Subsystem for Linux).

To run in Windows CMD shell:
* open a CMD window as Administrator (to support symlinks)
* python -m venv venv
* venv\Scripts\activate.bat
* pip install -r requirements.txt
* update the .env file with your Hugging Face api key
* python huggingface.py

To run in a Codespace (Linux) or WSL window:
* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* update the .env file with your Hugging Face api key
* python huggingface.py
