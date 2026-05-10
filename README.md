**Serene Plummer**

Project: NLP - Emotion Detection

This repository contains a small Flask app and emotion detection utilities.

Output screenshots
- [Screenshot 2026-05-08 22:04:41](output/Screenshot%202026-05-08%20220441.png)
- [Screenshot 2026-05-08 22:03:20](output/Screenshot%202026-05-08%20220320.png)
- [Screenshot 2026-05-08 22:01:41](output/Screenshot%202026-05-08%20220141.png)

How to run (local venv)

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

What I made
- A small Flask-based web UI (`/`) and an API endpoint (`/emotionDetector`) that accepts text and returns an emotion report.
- An `emotion_detection` module that: uses a persistent `requests.Session` for remote API calls, caches results with a thread-safe TTL cache, and falls back to a simple local heuristic scorer when the remote service is disabled or unreachable.
- Simple UI script (`static/mywebscript.js`) that calls the endpoint and displays the formatted result.
- Screenshots of runs are included in the `output/` folder.

Process (how I built it)
- Created the Flask app and basic HTML/JS UI to send text to the backend.
- Implemented the core emotion detection function that originally called the external Watson-like API.
- Made the system robust and faster by:
	- Adding a long-lived `requests.Session` to reuse TCP connections.
	- Adding a small in-memory TTL cache to avoid repeated identical calls.
	- Implementing a local heuristic fallback so the app remains responsive when the remote API times out or is disabled.
- Iteratively ran the Flask server locally, captured screenshots of the UI and error states, and fixed issues exposed by testing (decorator/syntax fixes, response formatting).
- Added environment variables for configuration: `EMOTION_ENABLE_REMOTE_API`, `EMOTION_API_URL`, `EMOTION_API_TIMEOUT_SECONDS`, `EMOTION_CACHE_TTL_SECONDS`.

If you'd like, I can also:
- Run the unit tests and record results in the README.
- Generate a `requirements.txt` from the venv.
- Add usage examples and sample curl commands.
