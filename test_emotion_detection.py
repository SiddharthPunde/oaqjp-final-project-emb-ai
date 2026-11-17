"""Unit tests for the emotion detection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify response parsing and error handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_joy(self, post):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "emotionPredictions": [{"emotion": {
                "anger": 0.01, "disgust": 0.02, "fear": 0.03,
                "joy": 0.90, "sadness": 0.04
            }}]
        }
        post.return_value = response
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, post):
        response = Mock(status_code=400)
        post.return_value = response
        result = emotion_detector("invalid text")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["joy"])

    def test_blank_text(self):
        result = emotion_detector("   ")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
