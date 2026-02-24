import os
from typing import override 
from groq import Groq
from dotenv import load_dotenv
import json
from IPython.display import Markdown, display

load_dotenv(override = True)
grok_key = os.getenv("GROQ_API_KEY")