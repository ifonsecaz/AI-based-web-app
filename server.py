''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from src.emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Method to call emotion_detector, and return the response
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    emotions = response

    # Check if the emotions is None, indicating an error or invalid input
    if emotions['dominant_emotions'] is None:
        return "Invalid text! Please try again."
    return (
        f'For the given statement, the system response is "anger":' 
        f'{emotions["anger"]}, "disgust": {emotions["disgust"]}, "fear": {emotions["fear"]}, '
        f'"joy": {emotions["joy"]} and "sadness": {emotions["sadness"]}. The dominant '
        f'emotion is {emotions["dominant_emotions"]}.'
    )

@app.route("/")
def render_index_page():
    """
    carga la pagina
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
