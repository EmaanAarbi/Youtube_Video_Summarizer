import os, tempfile, argparse, subprocess
from dotenv import load_dotenv
from pathlib import Path
import whisper  # ✅ Local Whisper
import google.generativeai as genai


# --- Load API key (optional, can also be passed from app.py) ---
load_dotenv()
DEFAULT_API_KEY = os.getenv("GEMINI_API_KEY")


# --- 1) Download audio from YouTube ---
def download_audio(url, output_path):
    output_file = os.path.join(output_path, "audio.%(ext)s")
    cmd = [
        "yt-dlp", "-x", "--audio-format", "mp3",
        "-o", output_file, url
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("✅ yt-dlp output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ yt-dlp failed with exit code:", e.returncode)
        print("---- STDOUT ----")
        print(e.stdout)
        print("---- STDERR ----")
        print(e.stderr)
        raise
    return os.path.join(output_path, "audio.mp3")



# --- 2) Transcribe with Whisper (LOCAL, no API required) ---
def transcribe(audio_file: str) -> str:
    print("🎙️ Transcribing with local Whisper...")
    model = whisper.load_model("small")  # tiny, base, small, medium, large
    result = model.transcribe(audio_file)
    return result["text"]


# --- 3) Summarize with Gemini ---
def summarize_text(text: str, style: str = "bullets", api_key: str = None) -> str:
    api_key = api_key or DEFAULT_API_KEY
    if not api_key:
        raise ValueError("❌ No Gemini API key provided! Set GEMINI_API_KEY in .env or pass it directly.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are a helpful note-taker.
    Summarize the following transcript into {style} format.

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text


# --- CLI Support ---
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True, help="YouTube video URL")
    p.add_argument("--style", default="bullets", choices=["bullets", "tldr", "notes"])
    p.add_argument("--out", default="summary.md")
    p.add_argument("--key", default=None, help="Gemini API Key (optional)")
    args = p.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        audio = download_audio(args.url, tmp)
        transcript = transcribe(audio)
        summary = summarize_text(transcript, args.style, api_key=args.key)

    Path(args.out).write_text(summary, encoding="utf-8")
    print(f"✅ Saved → {args.out}")
