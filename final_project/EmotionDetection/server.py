from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # 1. Retrieve the text from the UI input field
    text_to_analyze = request.args.get('textToAnalyze')

    # 2. Pass the text to your emotion detection function and get the result
    response = emotion_detector(text_to_analyze)

    # 3. Extract the individual emotion scores and the dominant emotion from the result
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # 4. Handle the "Invalid text" case 
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    
    # 5. Format the result into a user-friendly string and return it to the UI
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
