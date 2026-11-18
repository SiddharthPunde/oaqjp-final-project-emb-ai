# Final project

This repository contains a Python emotion-detection application built with the Watson NLP emotion prediction service and Flask.

## Features
- Detects anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion.
- Exposes a Flask web interface and JSON endpoint.
- Handles blank input and HTTP 400 responses.
- Includes unit tests for response parsing and error handling.

## Run locally

Install dependencies:

```bash
python -m pip install flask requests pylint
```

Start the application:

```bash
python server.py
```

Open `http://localhost:5001` in your browser.

Run unit tests:

```bash
python -m unittest -v
```

Run static analysis:

```bash
pylint server.py EmotionDetection test_emotion_detection.py
```
