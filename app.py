import streamlit as st
import tempfile
from summarize import summarize_text, transcribe, download_audio

st.set_page_config(page_title="YouTube Summarizer", page_icon="🎬", layout="centered")
st.title("🎬 YouTube Video Summarizer")
st.write("Paste a YouTube link and get both a transcript + AI-powered summary.")

# --- Input ---
url = st.text_input("🔗 Enter YouTube URL")
style = st.selectbox("📝 Summary Style", ["bullets", "tldr", "notes"])

# --- Run Button ---
if st.button("Summarize") and url:
    try:
        with tempfile.TemporaryDirectory() as tmp:
            st.info("⏳ Downloading audio from YouTube...")
            audio = download_audio(url, tmp)

            st.info("⏳ Transcribing with Whisper (local)...")
            text = transcribe(audio)
            st.success("✅ Transcription complete!")

            # Show transcript (optional)
            with st.expander("📜 Full Transcript"):
                st.text_area("Transcript", text, height=300)

            st.info("⏳ Summarizing with Gemini...")
            summary = summarize_text(text, style)
            st.success("✅ Summary ready!")

            st.subheader("📄 Summary")
            st.write(summary)

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
