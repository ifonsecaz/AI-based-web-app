from emotion_detection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy sentiment
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotions'], 'joy')
        
        # Test case for anger sentiment
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotions'], 'anger')
        
        # Test case for disgust sentiment
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotions'], 'disgust')

        # Test case for sadness sentiment
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotions'], 'sadness')

        # Test case for fear sentiment
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotions'], 'fear')

unittest.main()