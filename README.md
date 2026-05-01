# 🤖 Discord AI Chatbot (Powered by Groq)

An intelligent Discord chatbot powered by Large Language Models via the Groq API.  
The bot responds when mentioned, maintains short-term conversation context, and generates human-like replies in real time.

---

## 🚀 Features

- 💬 AI-powered responses using Groq LLMs  
- 🧠 Maintains chat history (context-aware replies)  
- 👀 Responds only when mentioned in Discord  
- ⚡ Ultra-fast inference using Groq API  
- 🔐 Secure API key management using `.env` file  
- 🔁 Continuous conversation flow support  

---

## 🏗️ Tech Stack

- Python 🐍  
- contentReference[oaicite:0]{index=0} API (`discord.py`)  
- contentReference[oaicite:1]{index=1} API  
- `python-dotenv` for environment variables  

---

## 📁 Project Structure

```bash
discord-ai-bot/
│── main.py              # Main bot logic
│── .env                 # API keys (not pushed to GitHub)
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```
---
##  🔐 Environment Variables Setup

Create a .env file in the root directory:
- SECRET_KEY=your_discord_bot_token
- GROQ_API_KEY=your_groq_api_key

## 💬 Example Usage
- User:
@RaaidGPT hello


- Bot:
Hello! How can I help you today?
