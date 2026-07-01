# Emotion Detector - Final Project

This is the **Final Project** (`oaqjp-final-project-emb-ai`) for the IBM Skills Network course *Developing AI Applications with Python and Flask*. A Flask web application that detects the emotion (anger, disgust, fear, joy, sadness) conveyed in a piece of text using the Watson NLP `EmotionPredict` service.

## Project Structure

- `EmotionDetection/` — application package (`emotion_detection.py` calls the Watson NLP service and formats the result)
- `server.py` — Flask web deployment (`/emotionDetector` endpoint and home page)
- `templates/index.html` — web UI
- `test_emotion_detection.py` — unit tests for the dominant emotion of five sample statements

## Running Locally

```bash
uv pip install -r requirements.txt
uv run python server.py
```

Then open `http://localhost:5000/` in a browser.

> Note: the Watson NLP `EmotionPredict` endpoint used by this project (`sn-watson-emotion.labs.skillsnetwork.site`) is only reachable from within the IBM Skills Network Cloud IDE lab environment.
