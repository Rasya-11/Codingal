import os
from pathlib import Path
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("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")

if not api_key:
    raise ValueError(
        f"GROQ_API_KEY is missing. Check this file: {env_path}")

client = Groq(api_key==api_key)
def generate