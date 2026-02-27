import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv
from prompt import Archit_Prompt, Alter_Archit_Prompt, JudgePrompt

load_dotenv(override=True)
groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

EGO_PROMPT = Archit_Prompt
ALTER_PROMPT = Alter_Archit_Prompt
JUDGE_PROMPT = JudgePrompt


# ==============================
# Response Generator
# ==============================

def generate_response(system_prompt, topic, previous_response=None):
    messages = [{"role": "system", "content": system_prompt}]

    if previous_response:
        messages.append({
            "role": "user",
            "content": f"""
Topic: {topic}
Previous Response: {previous_response}

Reply in 3-4 simple lines. Be clear and direct.
"""
        })
    else:
        messages.append({
            "role": "user",
            "content": f"""
Topic: {topic}

Reply in 3-4 simple lines. Be clear and direct.
"""
        })

    response = groq.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()


# ==============================
# Judge
# ==============================

def judge_debate(topic, debate_log):
    transcript = "\n".join(debate_log)

    judge_messages = [
        {"role": "system", "content": JUDGE_PROMPT},
        {
            "role": "user",
            "content": f"""
Topic: {topic}

Here is the full debate:

{transcript}

Ego speaks first and alternates with AlterEgo.

Who won? Give short reason.
"""
        }
    ]

    response = groq.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=judge_messages,
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


# ==============================
# Debate Engine (Sequential Format)
# ==============================

def run_debate(topic, rounds):
    debate_log = []
    chat_history = []
    previous = None

    for round_number in range(1, rounds + 1):

        # 🟢 Ego speaks
        ego_reply = generate_response(EGO_PROMPT, topic, previous)
        debate_log.append(f"Ego: {ego_reply}")

        chat_history.append({
            "role": "assistant",
            "content": f"🟢 **Optimistic Opinion (Round {round_number})**:\n\n{ego_reply}"
        })

        yield chat_history

        previous = ego_reply

        # 🔴 Alter counters
        alter_reply = generate_response(ALTER_PROMPT, topic, previous)
        debate_log.append(f"AlterEgo: {alter_reply}")

        chat_history.append({
            "role": "assistant",
            "content": f"🔴 **Sessimistic Opinion (Round {round_number})**:\n\n{alter_reply}"
        })

        yield chat_history

        previous = alter_reply

    # 🧑‍⚖️ Judge
    verdict = judge_debate(topic, debate_log)

    chat_history.append({
        "role": "assistant",
        "content": f"🧑‍⚖️ **Judge Verdict**:\n\n{verdict}"
    })

    yield chat_history


# ==============================
# UI
# ==============================

with gr.Blocks() as demo:

    gr.Markdown("# 🧠 DebateForge - Multi Agent AI Debate")

    topic_input = gr.Textbox(
        label="Debate Topic",
        placeholder="Enter debate topic..."
    )

    rounds_slider = gr.Slider(
        minimum=1,
        maximum=6,
        value=2,
        step=1,
        label="Number of Rounds"
    )

    debate_box = gr.Chatbot(label="Debate Arena")

    with gr.Row():
        start_btn = gr.Button("Start Debate")
        reset_btn = gr.Button("Reset")

    start_btn.click(
        run_debate,
        inputs=[topic_input, rounds_slider],
        outputs=debate_box
    )

    reset_btn.click(
        lambda: [],
        None,
        debate_box
    )

demo.launch(theme=gr.themes.Soft())