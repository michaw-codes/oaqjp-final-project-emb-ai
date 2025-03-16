import requests
import json

def emotion_detector(text_to_analyze):
    '''
    Takes text as an argument.
    Send the text to NLP service
    Returns the emotions object
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)

    emotions = {}
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = {
            "anger": formatted_response['emotionPredictions'][0]['emotion']['anger'],
            "disgust": formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            "fear": formatted_response['emotionPredictions'][0]['emotion']['fear'],
            "joy": formatted_response['emotionPredictions'][0]['emotion']['joy'],
            "sadness": formatted_response['emotionPredictions'][0]['emotion']['sadness'],
        }
        dominant_emotion = {"name": "", "score": 0}
        for emotion_name, emotion_score in emotions.items():
            if dominant_emotion["score"] < emotion_score:
                dominant_emotion["name"] = emotion_name
                dominant_emotion["score"] = emotion_score

        emotions["dominant_emotion"] = dominant_emotion["name"]
    elif response.status_code == 400:
        emotions = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    return emotions