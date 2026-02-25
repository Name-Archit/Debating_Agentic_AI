from prompt import Archit_Prompt
from prompt import Alter_Archit_Prompt
from prompt import Topic
from groq import Groq
from Main import Alter_ego, Debate

groq = Groq()

Alter_ego = Archit_Prompt


alterEgo_message = [
    {"role": "system", "content": Alter_ego},
    {"role": "user", "content": f"""Topic = {Topic} 
    response = {Debate[0]}
    Give your own opinion on why the response is in your opinion is not correct for the topic and make your opinion
    precise and easy to understand, opinion should be maximum 3-4 lines dont use heavy words and keep it simple, easy and clean."""}
]

alterEgo_response = groq.chat.completions.create(
    model = "openai/gpt-oss-20b",
    messages = alterEgo_message
)