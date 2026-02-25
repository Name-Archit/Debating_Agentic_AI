from prompt import Archit_Prompt
from prompt import Alter_Archit_Prompt
from prompt import Topic
from groq import Groq

groq = Groq()

Ego = Archit_Prompt

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