"""
server.py

This module contains the Flask web server application for the Emotion Detection system.
It handles HTTP GET requests, processes text for emotion analysis, and returns the results.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    This function handles the GET request to analyze the emotion of the provided text.
    It uses the emotion_detector function from the EmotionDetection package.
    If the input text is invalid, it returns an error message.
    Otherwise, it returns a formatted response with emotion scores and the dominant emotion.
    """
    # Get the text to analyze from the URL parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Run the emotion detection and get the status code
    result, status_code = emotion_detector(text_to_analyze)

    if status_code == 400:
        return "Invalid text! Please try again!"

    # Format the output as required
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
