import os
from typing import override 
from groq import Groq
from dotenv import load_dotenv
import json
from rich.console import Console
from rich.markdown import Markdown
from prompt import Archit_Prompt
from prompt import Alter_Archit_Prompt
from prompt import Topic
from Ego import Ego_response
from alterEgo import alterEgo_response

load_dotenv(override = True)
grok_key = os.getenv("GROQ_API_KEY")

Ego = Archit_Prompt
Alter_ego = Alter_Archit_Prompt
groq = Groq()
console = Console()

Debate = []

Ego_response1 = Ego_response.choices[0].message.content
Debate.append({"role": "assistant", "content": Ego_response1})

alterEgoResponse1 = alterEgo_response.choices[0].message.content
Debate.append({"role": "assistant", "content": alterEgoResponse1})

for message in Debate:
    print(message["content"])