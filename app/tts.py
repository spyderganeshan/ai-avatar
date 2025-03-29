from elevenlabs import ElevenLabs
import os
from config.settings import ELEVENLABS_API_KEY

def generate_speech(text):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio_stream = client.text_to_speech.convert(
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_multilingual_v2",
    )

    output_file = "static/output.mp3"
    with open(output_file, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    return output_file
