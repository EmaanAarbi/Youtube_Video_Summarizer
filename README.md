# 🎬 YouTube Video Summarizer

An **AI-powered YouTube Summarizer** that:
- Downloads video audio with `yt-dlp`  
- Transcribes locally using **OpenAI Whisper** (no API cost)  
- Generates concise summaries (**bullets, notes, or TL;DR**) with **Google Gemini AI**  
- Includes both a **Streamlit web app** and **CLI tool** for flexible usage  

---

## ✨ Features
- 🎙️ Local Whisper transcription (offline, no credits required)  
- 📝 Multiple summary styles: `bullets`, `tldr`, `notes`  
- 🎬 Streamlit interface for non-technical users  
- ⚡ CLI for fast terminal usage  

---
Environment Setup

Create a .env file in the root folder and add your Gemini API key:
    
    GEMINI_API_KEY=your_api_key_here

🚀 Usage
CLI

    python summarize.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --style bullets --out summary.md

Streamlit Web App

    streamlit run app.py


Paste a YouTube link in the app, and get both transcript + AI summary.

📂 Project Structure
      
    ├── app.py          # Streamlit web app
    ├── summarize.py    # CLI tool
    ├── requirements.txt
    ├── .env            # Gemini API key (not committed)
    └── README.md
⚡ Example Output

Input Video: https://www.youtube.com/watch?v=xxxx

Summary (bullets):

    Key idea 1
    Key idea 2
    Key idea 3

📜 License

    MIT License
    Free to use and modify.

## 🔧 Installation

```bash
# Clone this repo
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer

# Install dependencies
pip install -r requirements.txt

#Make sure you have yt-dlp installed:
pip install yt-dlp




