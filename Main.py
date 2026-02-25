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

load_dotenv(override = True)
grok_key = os.getenv("GROQ_API_KEY")

Ego = Archit_Prompt
Alter_ego = Alter_Archit_Prompt
Topic = Topic
groq = Groq()
console = Console()

Ego_message =[
    {"role": "system", "content": Ego},
    {"role": "user", "content": f"""Topic = {Topic} 
    make your output very precise and to the point maybe under 3-4 lines dont use 
    heavy words make it simple, easy and clean."""}
]

Ego_response = groq.chat.completions.create(
    model = "openai/gpt-oss-20b",
    messages = Ego_message
)

Ego_response1 = Ego_response.choices[0].message.content
console.print(Markdown(Ego_response1))

