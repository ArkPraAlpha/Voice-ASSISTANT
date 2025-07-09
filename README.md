# 🧠 Friday - Your Personal AI Assistant

This is a Python-based AI assistant, capable of:

- 🔍 Searching the web  
- 🌤️ Weather checking
- 📨 Sending Emails 
- 📷 Vision through camera (Web app
- 🗣️ Speech
- 📝 Chat (Web app) 

## 🛠 Requirements

- Python 3.10+
- Chrome & Brave (installed)
- WhatsApp (via Microsoft Store)
- Gmail account with App Password
- `.env` file with credentials (see below)

## 📦 Installation

```bash
git clone https://github.com/your-repo/friday-assistant
cd friday-assistant

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # on Windows

# Install requirements
pip install -r requirements.txt

## Running the Assistant

1. Development Mode (LiveKit)

python agent.py dev  #  This launches your LiveKit agent that can be connected from the Playground.

2. Console (TERMINAL)

python agent.py console # This runs in terminal
