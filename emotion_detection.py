import requests

def emotion_detector(text_to_analyse):
    # API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers including the model ID
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Send the request to the Watson NLP API
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        emotion_result = response.json()
        return emotion_result
    else:
        # Handle the error case
        raise Exception(f"Status code: {response.status_code}, Response: {response.text}")