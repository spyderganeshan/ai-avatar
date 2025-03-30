import requests
import io
from config.settings import DID_API_KEY,STATUS_URL,CREATE_AVATAR_URL,UPLOAD_URL
from loguru import logger

def upload_audio(audio_stream: io.BytesIO) -> str:
    """
    Uploads an audio file to the D-ID API and returns the URL.
    Args:
        audio_stream (io.BytesIO): The audio data stream to be uploaded.
    Returns:
        str: The URL of the uploaded audio.
    """
    headers = {"Authorization": f"Basic {DID_API_KEY}"}
    files = {"audio": ("speech.mp3", audio_stream, "audio/mpeg")}
    
    logger.info(f"senting post request to {UPLOAD_URL}", )
    response = requests.post(UPLOAD_URL, headers=headers, files=files)

    if response.status_code == 201:
        logger.info("Audio uploaded successfully")
        return response.json()["url"]
    else:
        logger.error(f"Error uploading audio: {response.text}")
        raise Exception(f"Error uploading audio: {response.text}")

def generate_avatar(audio_url: str) -> str:
    """
    Generates an avatar using the uploaded audio URL.
    Args:
        audio_url (str): The URL of the uploaded audio.
    Returns:
        str: The ID of the created avatar.
    """
    headers = {"Authorization": f"Basic {DID_API_KEY}"}
    payload = {
        "script": {"type": "audio", "audio_url": audio_url},
        "presenter_id": "amy-Aq6OmGZnMt",
        "driver_id": "Vcq0R4a8F0",
    }
    logger.info(f"senting post request to {CREATE_AVATAR_URL}", )
    response = requests.post(CREATE_AVATAR_URL, json=payload, headers=headers)

    if response.status_code == 201:
        logger.info("Avatar created successfully")
        return response.json()["id"]
    else:
        logger.error(f"Error creating avatar: {response.text}", )
        raise Exception(f"Error creating avatar: {response.text}")

def get_avatar_video(talk_id: str) -> str:
    """
    Retrieves the video URL for the generated avatar.
    Args:
        talk_id (str): The ID of the generated avatar.
    Returns:
        str: The URL of the generated video if available, otherwise None.
    """
    status_url = f"{STATUS_URL}/{talk_id}"
    headers = {"Authorization": f"Basic {DID_API_KEY}"}
    logger.info(f"senting get request to {status_url}", )
    response = requests.get(status_url, headers=headers)
    
    if response.status_code == 200:
        logger.info("Video URL retrieved successfully")
        data = response.json()
    else:
        logger.error(f"Error retrieving video URL: {response.text}")
        raise Exception(f"Error retrieving video URL: {response.text}")
    if "result_url" in data:
        return data["result_url"]
    else:
        return None
