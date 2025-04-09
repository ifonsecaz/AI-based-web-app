import json
from emotion_detection.emotion_detection import emotion_detector

response = emotion_detector("I am so happy I am doing this")

#formatted_response = json.loads(response)
print(response)