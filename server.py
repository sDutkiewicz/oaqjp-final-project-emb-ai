from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    # Get the text to analyze from the URL parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Run the emotion detection and get the status code
    result, status_code = emotion_detector(text_to_analyze)

    if status_code == 400:  # If input is invalid
        return "Invalid text! Please try again!"

    # Formatting the output
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
