# accessLlamaModelOnHuggingFace
This project tests accessing a Llama model on Hugging Face using an API key, since there are multiple (confusing) steps for successful authentication.

To run in a Codespace (Linux):
* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* if desired, update the .env file with your Hugging Face api key, else use the one already in the Codespace secret
* python HuggingFace.py

I do not recommend running this in Windows, as it takes a long time to download the needed files, and it locks up Windows.
To run in Windows CMD shell:
* open a CMD window as Administrator (to support symlinks)
* python -m venv venv
* venv\Scripts\activate.bat
* pip install -r requirements.txt
* update the .env file with your Hugging Face api key
* python HuggingFace.py

When you first run it in a Codespace, it will take some time to download 20GB of files. I have since updated the model to a smaller one that downloads about 2GB of files (vs 20GB).

<img src="https://github.com/user-attachments/assets/a0074f76-e163-4176-915f-a8ad753736f3" alt="Image description" width="750">

Once you have an account on Hugging Face, you still need to request access to a specific model:

<img src="https://github.com/user-attachments/assets/8e228964-a577-4b13-a780-dd4ddddf7f28" alt="Image description" width="750">

When your access is granted, you will receive an email like this:

<img src="https://github.com/user-attachments/assets/df9eba9c-6d0b-4187-8dc3-a57864666f7d" alt="Image description" width="400">

When you create a token, be sure to give it Write access:

<img src="https://github.com/user-attachments/assets/6a241066-d029-477a-8880-f80965ce4365" alt="Image description" width="600">

