from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text to analyze as a query param and 
        runs emotion_detector function.
        Returns formatted text with emotion analysis.
    '''

    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    print(response)
    if not response:
        return "Invalid input ! Try again."

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)