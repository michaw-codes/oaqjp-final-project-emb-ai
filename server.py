''' Runs the emotion detection application on Flask server on localhost:5000.'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text to analyze as a query param and runs emotion_detector function.
        Returns formatted text with emotion analysis.
    '''

    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}  and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
