"""Flask web application for emotion detection."""

import requests
from flask import Flask, jsonify, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def root():
    """Render the application home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze supplied text and return emotion scores as JSON."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return jsonify({"error": "Please enter some text to analyze."}), 400

    try:
        result = emotion_detector(text_to_analyze)
    except requests.RequestException:
        return jsonify({"error": "The emotion service is currently unavailable."}), 502
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Unable to analyze the supplied text."}), 502

    if result.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text. Please try again."}), 400
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
