import io                                               # handling in-memory byte streams.
from elevenlabs import ElevenLabs                       # Importing ElevenLabs for text-to-speech conversion.          
from config.settings import ELEVENLABS_API_KEY,VOICE_ID,OUTPUT_FORMAT,MODEL_ID
from loguru import logger

def generate_speech(text: str) -> io.BytesIO:
    """
    Converts the given text into speech using ElevenLabs' text-to-speech API.
    Args:
        text (str): The input text to be converted into speech.
    Returns:
        io.BytesIO: An in-memory byte stream containing the generated speech in MP3 format.
    """
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    logger.info("client created")
    audio_stream        = client.text_to_speech.convert(
        voice_id        =VOICE_ID,
        output_format   =OUTPUT_FORMAT,
        text            =text,
        model_id        =MODEL_ID,
    )

    audio_bytes = io.BytesIO()
    for chunk in audio_stream:
        audio_bytes.write(chunk)                        # Write chunk-by-chunk to memory
    audio_bytes.seek(0)                                 # Reset stream position for reading
    logger.info("Speech generation completed in memory")
    return audio_bytes                                  # Return BytesIO object instead of file path
