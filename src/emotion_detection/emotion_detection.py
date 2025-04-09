import requests
import json

def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj= { "raw_document": { "text": text_to_analyse } }
   
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    emotions={}
    label=""
    score=0
    if response.status_code == 200:
        for emotion in formatted_response['emotionPredictions'][0]['emotion'].keys():
            emotions[emotion]=formatted_response['emotionPredictions'][0]['emotion'][emotion]
            if(score<formatted_response['emotionPredictions'][0]['emotion'][emotion]):
                score=formatted_response['emotionPredictions'][0]['emotion'][emotion] 
                label=emotion
        emotions['dominant_emotions']=label
    elif response.status_code == 400:
        emotions['anger']=None
        emotions['disgust']=None
        emotions['fear']=None
        emotions['sadness']=None
        emotions['dominant_emotions']=None
    elif response.status_code == 500:
        emotions=None  

    return emotions