from elevenlabs import ElevenLabs
import os
from config.settings import ELEVENLABS_API_KEY
from loguru import logger

def generate_speech(text):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    logger.info("client created")
    audio_stream = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_multilingual_v2",
    )

    output_file = "static/output.mp3"
    with open(output_file, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
        logger.info("speech file created")
    return output_file
