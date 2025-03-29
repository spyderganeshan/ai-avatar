import requests
import os
from config.settings import DID_API_KEY

UPLOAD_URL = "https://api.d-id.com/audios"
CREATE_AVATAR_URL = "https://api.d-id.com/clips"

def upload_audio(audio_path):
    headers = {"Authorization": f"Basic {DID_API_KEY}"}

    with open(audio_path, "rb") as audio_file:
        files = {"audio": (audio_path, audio_file)}
        response = requests.post(UPLOAD_URL, headers=headers, files=files)

    if response.status_code == 201:
        return response.json()["url"]
    else:
        raise Exception(f"Error uploading audio: {response.text}")

def generate_avatar(audio_url):
    headers = {"Authorization": f"Basic {DID_API_KEY}"}
    payload = {
        "script": {"type": "audio", "audio_url": audio_url},
        "presenter_id": "amy-Aq6OmGZnMt",
        "driver_id": "Vcq0R4a8F0",
    }
    response = requests.post(CREATE_AVATAR_URL, json=payload, headers=headers)

    if response.status_code == 201:
        return response.json()["id"]
    else:
        raise Exception(f"Error creating avatar: {response.text}")

def get_avatar_video(talk_id):
    status_url = f"https://api.d-id.com/clips/{talk_id}"
    headers = {"Authorization": f"Basic {DID_API_KEY}"}
    response = requests.get(status_url, headers=headers)
    data = response.json()

    if "result_url" in data:
        return data["result_url"]
    else:
        return None
