from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    # Get the text to analyze from the URL parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    if text_to_analyze:
        # Run the emotion detection
        result = emotion_detector(text_to_analyze)

        # Format the output as required
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text
    else:
        return "Error: No text provided for analysis."

if __name__ == "__main__":
    app.run(port=5000)
