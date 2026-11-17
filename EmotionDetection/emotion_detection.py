"""Call the Watson NLP emotion prediction service."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for input text.

    A service response with HTTP 400 returns None for every score and
    dominant_emotion, as required by the project specification.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {**{emotion: None for emotion in EMOTIONS}, "dominant_emotion": None}

    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        URL, headers=HEADERS, json=payload, timeout=30
    )

    if response.status_code == 400:
        return {**{emotion: None for emotion in EMOTIONS}, "dominant_emotion": None}

    response.raise_for_status()
    predictions = response.json().get("emotionPredictions", [])
    if not predictions:
        raise ValueError("The emotion service returned no predictions.")

    scores = predictions[0].get("emotion", {})
    result = {emotion: scores.get(emotion) for emotion in EMOTIONS}
    available_scores = {key: value for key, value in result.items() if value is not None}
    result["dominant_emotion"] = (
        max(available_scores, key=available_scores.get) if available_scores else None
    )
    return result
