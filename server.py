"""
Flask server for Emotion Detection application.
This server exposes endpoints to analyze text emotion using Watson NLP.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests from the web interface.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    # Handle invalid or blank input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
