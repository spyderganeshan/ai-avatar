# Test-to-speech AI Avatar

This project integrates a synthetic voice with a virtual avatar to generate synchronized facial animations using text input. It leverages ElevenLabs for text-to-speech (TTS) and D-ID for avatar animations. The interface is built using Streamlit.

### Features

- Text-to-Speech conversion using ElevenLabs API

- Avatar animation with synchronized speech using D-ID API

- Simple web-based UI using Streamlit

- Configuration management via settings.py

- Secure API key handling using .env file

### Requirements

- Python 3.8+

- Virtual environment (venv)

- Dependencies listed in requirements.txt

### Setup

Clone the repository:

```
git clone <repository-url>
cd <repository-folder>
```

Create and activate a virtual environment:
```
python -m venv venv
venv/bin/activate  
```

Install dependencies:
```
pip install -r requirements.txt
```
Set up environment variables:

Create a .env file and add API keys:
```
ELEVENLABS_API_KEY=your_elevenlabs_api_key
D_ID_API_KEY=your_did_api_key
PIN=password
```
Configure settings:

Update settings.py with necessary URLs and configurations.

### Usage

Run the Streamlit app:
```
streamlit run app.py
```
Enter the pin to access the app and Enter text input in the web UI.
The avatar will generate facial animations synchronized with the TTS output

### File Structure
```
├── app.py               # Main Streamlit app
├── avatar.py            # Handle D-ID API
├── tts.py               # Handle TTS output
├── config/settings.py   # Configuration file 
├── .env                 # Env variables (API keys)
├── requirements.txt     # Required dependencies
├── venv/                # Virtual environment (ignored in Git)
└── README.md            # Project documentation
```
Notes:
``
Ensure that your API keys are valid and have sufficient quota.
The implementation prioritizes functionality over low-latency optimization.
``

### Future Enhancements

- Improve animation synchronization.

- Add speech-to-text functionality.

- Optimize for real-time performance.

### License

This project is for educational and development purposes only. Ensure compliance with the terms of use of the APIs used.

Author

Ganeshan P


