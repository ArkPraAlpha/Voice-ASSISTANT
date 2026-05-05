# 🧠 Friday - Your Personal AI Voice Assistant

Friday is a Python-based, voice-interactive AI assistant inspired by the AI from Iron Man. Built on top of [LiveKit Agents](https://github.com/livekit/agents), Friday features a classy butler persona, capable of conversing naturally and executing a variety of helpful tasks.

## ✨ Features

- **🗣️ Natural Voice Interaction**: Powered by Google's RealtimeModel for seamless speech-to-speech interaction with a sophisticated and slightly sarcastic persona.
- **🌐 Smart Web Search**: Searches the web using DuckDuckGo, with automatic fallback to Google Custom Search API.
- **📧 Advanced Email Management**: 
  - Send emails via your Gmail account.
  - Interactive voice-based email drafting (specify recipient, subject, and message).
  - AI-assisted message generation based on natural language prompts (e.g., "Write a professional message about a project delay").
- **🌤️ Weather Checking**: Real-time weather updates using `wttr.in`.
- **💻 App Launcher**: Opens specific applications and websites seamlessly:
  - **YouTube**: Opens YouTube and performs searches (defaults to Brave browser if available).
  - **Gmail**: Opens Gmail in Chrome.
  - **WhatsApp**: Launches the WhatsApp Desktop application on Windows.

## 🛠 Prerequisites

- **Python**: Version 3.10 or higher.
- **Browsers**: Chrome and/or Brave (for app launching capabilities).
- **WhatsApp**: Installed via the Microsoft Store.
- **Gmail Account**: Requires an App Password for SMTP email sending.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory and add the following configuration variables:

```env
# LiveKit Configuration (Required for LiveKit connection)
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret

# Google API Credentials (For Search)
GOOGLE_SEARCH_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id

# Gmail SMTP Configuration (For sending emails)
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
```

## 🚀 Running the Assistant

You can run the assistant in development mode connected to the LiveKit sandbox/cloud:

```bash
python agent.py dev
```

To run in your terminal:

```bash
python agent.py start
```

## 📂 Project Structure

- `agent.py`: The core LiveKit agent implementation, containing chat hooks and the main logic for processing user commands.
- `newtool.py`: Defines the function tools available to the assistant (web search, weather, email).
- `tool_app_launcher.py`: Functions to open external applications like YouTube, Gmail, and WhatsApp.
- `prompts.py`: Contains the system instructions and persona details for Friday.
- `helper.py`: Provides utility functions, like generating email bodies from prompts using the LLM.
