import streamlit as st
from app.tts import generate_speech
from app.avatar import upload_audio, generate_avatar, get_avatar_video
import time

st.set_page_config(page_title="AI Avatar Generator", layout="centered")

st.title("🎭 AI Avatar Generator")
st.write("Enter text, generate a talking AI avatar, and watch the result!")

text_input = st.text_area("Enter your text:", height=100)

if st.button("Generate Avatar"):
    if text_input.strip():
        with st.spinner("Generating speech..."):
            audio_file = generate_speech(text_input)

        with st.spinner("Uploading audio..."):
            audio_url = upload_audio(audio_file)

        with st.spinner("Creating avatar..."):
            talk_id = generate_avatar(audio_url)

        st.success("Avatar is being generated. Please wait...")

        # Polling for video URL
        video_url = None
        for _ in range(30):  # Check for up to 30 seconds
            time.sleep(3)
            video_url = get_avatar_video(talk_id)
            if video_url:
                break

        if video_url:
            st.video(video_url)
            st.download_button("Download Video", video_url, file_name="avatar.mp4")
        else:
            st.error("Failed to generate avatar. Try again later.")
    else:
        st.warning("Please enter some text.")
