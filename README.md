# Day 7: YouTube Video Q&A Bot 🎥🤖

An advanced AI-powered tool that allows you to "talk" to any YouTube video! This bot fetches the transcript, builds a semantic knowledge base (RAG), and lets you ask questions about the video's content using the **Groq Llama-3.3-70b** model for lightning-fast answers.

## ✨ Features
- **Smart Transcript Fetching**: Uses `youtube-transcript-api` to extract text from videos with English CC.
- **RAG Architecture**: Implements Retrieval-Augmented Generation using LangChain and ChromaDB.
- **AI-Powered Answers**: Uses Groq's `llama-3.3-70b-versatile` model for high-quality, relevant responses.
- **Instant Summarization**: Automatically generates a 5-bullet-point summary of the video.
- **Interactive CLI**: Easy-to-use command-line interface.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/gnarendra9014-blind/day_7-of-ML-Projects.git
   cd day_7-of-ML-Projects
   ```

2. **Create and Activate a Virtual Environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_api_key_here
   ```

## 🚀 How to Run
Once your environment is set up and active, start the bot:
```powershell
python app.py
```
- Paste a YouTube URL when prompted.
- View the auto-generated summary.
- Ask questions about the video! Type `quit` to exit.

## 🔧 Core Components
- **`app.py`**: The main interface for the application.
- **`transcript.py`**: Handles video ID extraction and transcript fetching logic.
- **`rag.py`**: Implements the Retrieval-Augmented Generation logic, from vectorstore creation to AI responses.
- **`requirements.txt`**: List of all necessary Python libraries.

---
Part of the **25 Days of ML Projects** challenge. Built for learning and experimentation!
