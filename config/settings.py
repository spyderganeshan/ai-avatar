import os
from dotenv import load_dotenv

load_dotenv()

PIN                 = os.getenv("PIN")
ELEVENLABS_API_KEY  = os.getenv("ELEVENLABS_API_KEY")
DID_API_KEY         = os.getenv("DID_API_KEY")
VOICE_ID            = "21m00Tcm4TlvDq8ikWAM"
OUTPUT_FORMAT       = "mp3_44100_128"
MODEL_ID            = "eleven_multilingual_v2"
CREATE_AVATAR_URL   = "https://api.d-id.com/clips"
UPLOAD_URL          = "https://api.d-id.com/audios"
STATUS_URL          = "https://api.d-id.com/clips"
