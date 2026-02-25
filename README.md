# Debating Agentic AI

Two AI agents. One topic. Structured opposition.
A neutral judge decides who argues better.

This project simulates a controlled debate between autonomous AI roles using the **GROQ** inference platform and the `openai/gpt-oss-20b` model. The system explores how a single language model can adopt contrasting perspectives, sustain multi-turn reasoning, and later evaluate its own generated discourse.

Instead of a casual chatbot exchange, this project enforces a strict argumentative protocol — each response builds directly on the previous one, forming a structured chain of reasoning that culminates in a final judgment.

---

## How It Works

The system creates three distinct agents using role-based prompting:

* **Optimistic Agent** – Supports the topic.
* **Pessimistic Agent** – Challenges and critiques the topic.
* **Neutral Judge** – Evaluates both arguments and declares a winner.

All three agents use the same base model:

```
openai/gpt-oss-20b
```

Behavior differences emerge purely from prompt conditioning.

---

## Debate Structure

Each debate follows a fixed four-stage exchange:

1. **Opening Argument** – Optimistic agent presents its position.
2. **Counterargument** – Pessimistic agent responds directly.
3. **Rebuttal** – Optimistic agent addresses the critique.
4. **Final Response** – Pessimistic agent reinforces its objections.

After two complete back-and-forth exchanges, the full transcript is passed to the Neutral Judge.

The judge analyzes:

* Logical consistency
* Argument strength
* Relevance to the topic
* Persuasiveness

It then declares:

* The winner
* A reasoned explanation for the decision

No external scoring system is used — the evaluation is entirely model-driven.

---

## Conceptual Flow

```
User Topic
   ↓
Optimistic Argument
   ↓
Pessimistic Counter
   ↓
Optimistic Rebuttal
   ↓
Pessimistic Final Statement
   ↓
Neutral Judgment
```

Each step receives the complete prior context to maintain argumentative continuity.

---

## Tech Stack

* **Language:** Python
* **Environment:** UV (Python virtual environment)
* **Model Provider:** GROQ
* **Model Used:** `openai/gpt-oss-20b`
* **Architecture Style:** Role-based multi-agent simulation

---

## Setup

### Clone the repository

```bash
git clone https://github.com/your-username/debating-agentic-ai.git
cd debating-agentic-ai
```

### Create UV environment

```bash
uv venv
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
uv pip install -r requirements.txt
```

### Add GROQ API key

```bash
export GROQ_API_KEY="your_api_key"
```

Windows PowerShell:

```powershell
setx GROQ_API_KEY "your_api_key"
```

---

## Running the Project

```bash
python main.py
```

Enter a topic when prompted:

```
Is artificial intelligence beneficial for humanity?
```

The agents will debate automatically, and the judge will declare a winner.

---

This is not just a chatbot — it is a constrained argumentative system where reasoning competes.

---
