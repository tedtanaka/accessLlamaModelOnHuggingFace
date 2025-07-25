import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
hf_access_token = os.environ.get("HF_TOKEN")

# login(token = hf_access_token)

# Specify a cache directory
cache_dir = os.path.join(os.getcwd(), "model_cache")

# I don't have access to this model
# model_name = "meta-llama/Llama-2-7b-chat-hf"

# This model is large and takes a long time to download
# model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

# Try this smaller model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir, token=hf_access_token)
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir, token=hf_access_token)

def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_length=100)
    return tokenizer.decode(output[0], skip_special_tokens=True)

prompt = "Hello, how are you?"
result = generate_text(prompt)
print(result)
