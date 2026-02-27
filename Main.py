import os
from typing import override 
from groq import Groq
from dotenv import load_dotenv
import json
from rich.console import Console
from rich.markdown import Markdown
from prompt import Archit_Prompt, Alter_Archit_Prompt, Topic, JudgePrompt

load_dotenv(override = True)
grok_key = os.getenv("GROQ_API_KEY")

Ego = Archit_Prompt
Alter_ego = Alter_Archit_Prompt
judge = JudgePrompt

groq = Groq()
console = Console()

Debate = []

flag = 0

def architAlter(term, word):
    if word == "alter":
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

        alterEgoResponse1 = alterEgo_response.choices[0].message.content
        Debate.append({"role": "assistant", "content": alterEgoResponse1})

    elif word == "alterDebate":        

        alterEgo_message_Debate = [
        {"role": "system", "content": Alter_ego},
        {"role": "user", "content": f"""Topic = {Topic} 
        response = {Debate[term]}
        Give your own opinion on why the response is in your opinion is not correct for the topic and make your opinion
        precise and easy to understand, opinion should be maximum 3-4 lines dont use heavy words and keep it simple, easy and clean."""}
        ]

        alterEgo_response_Debate = groq.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = alterEgo_message_Debate
        )

        alterEgoResponses = alterEgo_response_Debate.choices[0].message.content
        Debate.append({"role": "assistant", "content": alterEgoResponses})

def architEgo(term, word):

    if word == "ego":
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
        Debate.append({"role": "assistant", "content": Ego_response1})

    elif word == "egoDebate":
        Ego_message_Debate =[
        {"role": "system", "content": Ego},
        {"role": "user", "content": f"""Topic = {Topic} 
        response = {Debate[term]}
        make your output very precise and to the point maybe under 3-4 lines dont use 
        heavy words make it simple, easy and clean."""}
        ]

        Ego_response_Debate = groq.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = Ego_message_Debate
        )

        Ego_responses = Ego_response_Debate.choices[0].message.content
        Debate.append({"role": "assistant", "content": Ego_responses})

def Judgement(Debate):
    judge_message = [
        {"role": "system", "content": judge},
        {"role": "user", "content": f"""Topic = {Topic},
        responses = {Debate}
        
        In the list named as Debate all the even indexed responses are of Ego responses and all the odd ones
        are of alterEgo responses according to the topic give your verdict who is correct Ego or alterEgo and 
        also in simple and to the point reason why you think your choice is correct and other is wrong."""}
    ]

    JudgeResponse = groq.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = judge_message
    )

    judgeResponses = JudgeResponse.choices[0].message.content
    return judgeResponses

print("How many round you want the debate to happen: ")
n = int(input())

term = 0
architEgo(term, "ego")
architAlter(term, "alter")

n -= 1

while n != 0 :
    if flag == 0:
        term += 1
        architEgo(term, "egoDebate")
        flag = 1

    else:
        term += 1
        architAlter(term, "alterDebate")
        flag = 0

    n-=1

console.print(Markdown(Judgement(Debate)))


