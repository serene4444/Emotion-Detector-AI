**Serene Plummer**

Project: NLP - Emotion Detection

AI / Machine Learning concepts used
- Natural language processing to analyze text for emotion cues.
- Emotion classification into `joy`, `anger`, `disgust`, `sadness`, and `fear`.
- A dominant-emotion decision step that selects the strongest predicted label.
- A fallback scoring approach so the app still responds when the remote model is unavailable.
- Basic API-driven inference, where text is sent to a model endpoint and the response is converted into a user-friendly report.

This repository contains a small Flask app and emotion detection utilities.

Output screenshots
![You shouldn't chew with your mouth open when you eat..png](output/You%20shouldn't%20chew%20with%20your%20mouth%20open%20when%20you%20eat..png)
![I think I'm having fun.png](output/I%20think%20I'm%20having%20fun.png)
![Artemis II's takeoff was so cool, I loved the pictures!.png](output/Artemis%20II's%20takeoff%20was%20so%20cool%2C%20I%20loved%20the%20pictures!.png)

What I made
- A small Flask-based web UI (`/`) and an API endpoint (`/emotionDetector`) that accepts text and returns an emotion report.
- An `emotion_detection` module that uses a remote API when enabled and a local fallback when the service is unavailable.
- Simple UI script (`static/mywebscript.js`) that calls the endpoint and displays the formatted result.
- Screenshots of runs are included in the workspace.

Process (how I built it)
- Created the Flask app and basic HTML/JS UI to send text to the backend.
- Implemented the core emotion detection function that originally called the external Watson-like API.
- Made the system reliable by adding a local fallback so the app remains responsive when the remote API times out or is disabled.
- Iteratively ran the Flask server locally, captured screenshots of the UI and error states, and fixed issues exposed by testing.
- Added environment variables for configuration: `EMOTION_ENABLE_REMOTE_API`, `EMOTION_API_URL`, `EMOTION_API_TIMEOUT_SECONDS`, `EMOTION_CACHE_TTL_SECONDS`.

How to run
1. Create and activate a virtual environment (Windows PowerShell example):

```
python -m venv .venv
& ".venv\Scripts\Activate.ps1"
```

2. Install dependencies:

```
pip install -r final_project/requirements.txt
```

3. Run the Flask app from `final_project`:

```
cd final_project
python -m flask --app EmotionDetection.server run --host localhost --port 5000
```

Configuration
- `EMOTION_ENABLE_REMOTE_API`: set to `1` or `true` to enable remote API calls (default off).
- `EMOTION_API_URL`: override remote API URL.
- `EMOTION_API_TIMEOUT_SECONDS`: per-request timeout when calling remote API.
- `EMOTION_CACHE_TTL_SECONDS`: TTL for in-memory cache (seconds).

Notes
- Local fallback scorer is used when remote API is disabled or unreachable.

