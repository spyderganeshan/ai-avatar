import  time
import  streamlit as st
from tts    import generate_speech
from avatar import upload_audio, generate_avatar, get_avatar_video
from loguru import logger
from config.settings import PIN
st.set_page_config(page_title="AI Avatar Generator", layout="centered")

###################################### authentication settings #####################################
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if not st.session_state.authenticated:
    user_pin = st.text_input("Enter Access PIN:", type="password")
    if user_pin:  
        if user_pin == PIN:
            st.session_state.authenticated = True
            st.rerun()  
        else:
            st.warning("Incorrect PIN. Please try again.")
            st.stop()
    else:
        st.stop()  

######################################### app layout ################################################
st.title("🎭 AI Avatar Generator")
st.write("Enter text, generate a talking AI avatar, and watch the result!")

text_input = st.text_area("Enter your text:", height=100)

if st.button("Generate Avatar"):
    if text_input.strip():
        with st.spinner("Generating speech..."):
            logger.info("Generating speech...")
            audio_file = generate_speech(text_input)

        with st.spinner("Uploading audio..."):
            logger.info("Uploading audio...")
            audio_url = upload_audio(audio_file)

        with st.spinner("Creating avatar..."):
            logger.info("Creating avatar...")
            talk_id = generate_avatar(audio_url)

        st.success("Avatar is being generated. Please wait...")

        # Polling for video URL
        video_url = None
        with st.spinner("Checking for video URL..."):
            for _ in range(30):  # Check for up to 30 seconds
                time.sleep(3)
                logger.info("Checking for video URL...")
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