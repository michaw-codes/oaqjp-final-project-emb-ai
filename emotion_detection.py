import requests

def emotion_detector(text_to_analyze):
    '''
    Takes text as an argument.
    Send the text to NLP service
    Returns the text attribute of the response object
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)

    return response.text