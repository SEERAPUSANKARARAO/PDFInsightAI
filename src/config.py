from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    config = {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "google_api_key": os.getenv("GOOGLE_API_KEY")
    }
    return config
