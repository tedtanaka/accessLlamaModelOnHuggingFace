# accessLlamaModelOnHuggingFace
This project tests accessing a Llama model on Hugging Face using an API key, since there are multiple (confusing) steps for successful authentication.

To run in a Codespace (Linux):
* Create a Codespace with 8 cores (not the default 2 cores)
* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* if desired, update the .env file with your Hugging Face api key, else use the one already in the Codespace secret
* python HuggingFace.py

To run in Windows CMD shell:
* open a CMD window as Administrator (to support symlinks)
* python -m venv venv
* venv\Scripts\activate.bat
* pip install -r requirements.txt
* update the .env file with your Hugging Face api key
* python HuggingFace.py

The 2GB model runs on Windows and an 8-core Codespace.  The 20GB model may not, though.

<img src="https://github.com/user-attachments/assets/a0074f76-e163-4176-915f-a8ad753736f3" alt="Image description" width="750">

# Creating your own key
You can use my Hugging Face key (in a Codespace secret), but if you want your own, follow these steps.  First, create an account on Hugging Face.

Once you have an account on Hugging Face, find the model and request access to it.  You will need to fill in your name and other details, and accept the license terms:

<img src="https://github.com/user-attachments/assets/8e228964-a577-4b13-a780-dd4ddddf7f28" alt="Image description" width="750">

When your access is granted, you will receive an email like this:

<img src="https://github.com/user-attachments/assets/df9eba9c-6d0b-4187-8dc3-a57864666f7d" alt="Image description" width="400">

When you create a token, be sure to give it Write access:

<img src="https://github.com/user-attachments/assets/6a241066-d029-477a-8880-f80965ce4365" alt="Image description" width="600">

