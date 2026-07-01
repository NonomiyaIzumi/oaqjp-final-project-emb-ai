"""Unit tests for the emotion_detector function."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verify the dominant emotion detected for sample statements."""

    def test_emotion_detection(self):
        """Each sample statement should map to its expected dominant emotion."""
        result = emotion_detector("I am so happy I am doing this")
        self.assertEqual(result["dominant_emotion"], "joy")

        result = emotion_detector("I am so angry I could scream")
        self.assertEqual(result["dominant_emotion"], "anger")

        result = emotion_detector("I am so disgusted by this")
        self.assertEqual(result["dominant_emotion"], "disgust")

        result = emotion_detector("I am so scared and afraid")
        self.assertEqual(result["dominant_emotion"], "fear")

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
