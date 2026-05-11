NLP - Emotion Detection 🎯

**Course:** Developing AI Applications with Python and Flask

**Created by:** Serene Plummer

---

## 🎯 Project Overview

This project builds a real-time emotion detection web application that analyzes user-provided text and classifies it into one of five emotional categories: **joy**, **anger**, **disgust**, **sadness**, and **fear**. The system uses natural language processing (NLP) to extract emotion cues and a dominant-emotion decision step to select the strongest predicted label. A local fallback scorer ensures the application remains responsive even when the remote AI service is unavailable.

## 📁 Data & Project Assets

The repository includes application code and output samples:

- **`final_project/EmotionDetection/emotion_detection.py`** — Core NLP module with local fallback scorer and remote API integration.
- **`final_project/EmotionDetection/server.py`** — Flask application with web UI route and API endpoint (`/emotionDetector`).
- **`final_project/templates/index.html`** — HTML interface for user text input.
- **`final_project/static/mywebscript.js`** — Client-side JavaScript for API calls and result rendering.
- **`output/`** — Sample emotion detection results with annotated screenshots.
- **`empty_input_error.png`** — Error handling demonstration (invalid/empty input).

## 🧰 Tools & Technologies

**Languages:** Python  
**Development Environment:** Jupyter Notebook, Git & GitHub  
**Framework & Libraries:**
- Flask — lightweight web framework
- requests — HTTP client for remote API calls
- threading, time — for concurrent caching and TTL management
- Custom keyword-based NLP scorer — local fallback when remote unavailable

**APIs:** Watson-like emotion detection endpoint (optional remote mode)  
**UI:** HTML5, vanilla JavaScript, CSS

## 🔍 Project Workflow & Learnings

1. **API Integration** — Connected to the external Watson emotion detection service; implemented timeout and error handling.
2. **Local Fallback Scorer** — Built a keyword-based heuristic scorer so the app works offline or when the remote service is down.
3. **Caching & Performance** — Added a thread-safe TTL cache to avoid repeated identical API calls.
4. **Error Handling** — Implemented graceful fallbacks for empty input, network failures, and invalid responses.
5. **Web UI Development** — Created a simple, responsive HTML interface with real-time feedback.
6. **Testing & Validation** — Ran unit tests to confirm emotion classification accuracy; captured screenshots of happy path and error states.

## 🎨 Output Samples

![You shouldn't chew with your mouth open when you eat..png](output/You%20shouldn't%20chew%20with%20your%20mouth%20open%20when%20you%20eat..png)  
![I think I'm having fun.png](output/I%20think%20I'm%20having%20fun.png)  
![Artemis II's takeoff was so cool, I loved the pictures!.png](output/Artemis%20II's%20takeoff%20was%20so%20cool%2C%20I%20loved%20the%20pictures!.png)  
![Empty input error screenshot](empty_input_error.png)

## 🚀 Quick Start

**1. Set up the virtual environment:**

```bash
python -m venv .venv
& ".venv\Scripts\Activate.ps1"  # Windows PowerShell
# or: source .venv/bin/activate  # Linux/macOS
```

**2. Install dependencies:**

```bash
pip install -r final_project/requirements.txt
```

**3. Run the Flask app:**

```bash
cd final_project
python -m flask --app EmotionDetection.server run --host localhost --port 5000
```

Open your browser to `http://localhost:5000` and enter text to analyze.

## ⚙️ Configuration

- **`EMOTION_ENABLE_REMOTE_API`**: Set to `1` or `true` to enable remote Watson API calls (default: `0` — uses local scorer).
- **`EMOTION_API_URL`**: Override the remote API endpoint URL.
- **`EMOTION_API_TIMEOUT_SECONDS`**: Per-request timeout for remote calls (default: `1.0` seconds).
- **`EMOTION_CACHE_TTL_SECONDS`**: Time-to-live for cached results (default: `300` seconds).

## 📝 Notes

- The local fallback scorer uses keyword matching for rapid responses when the remote service is unavailable.
- All emotion scores are normalized to a 0–1 range; the dominant emotion is selected as the highest-scoring category.
- Unit tests validate accuracy on sample test cases (see `final_project/EmotionDetection/test_emotion_detection.py`).

