import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(URL, json=input_json, headers=header)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        formated_response = response.json()
        return formated_response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
    except Exception as err:
        print(f"Other error occurred: {err}")
        return {
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }

def emotion_predictor(detected_text):
    if all(value is None for value in detected_text.values()):
        return detected_text
    
    if 'emotionPredictions' in detected_text and detected_text['emotionPredictions']:
        emotions = detected_text['emotionPredictions'][0]['emotion']
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        max_emotion = max(emotions, key=emotions.get)
        
        formated_dict_emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': max_emotion
        }
        return formated_dict_emotions
    
    return {
        'anger': None,
        'disgust': None, 
        'fear': None, 
        'joy': None, 
        'sadness': None, 
        'dominant_emotion': None
    }
