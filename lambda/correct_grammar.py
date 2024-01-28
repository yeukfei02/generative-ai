import boto3
import json

def handler(event, context):
    print(f"event = {event}")

    response = None

    if event:
        response = correct_grammar(event)

    return response

def correct_grammar(event):
    result = None

    try:
        client = boto3.client('bedrock-runtime')

        body = {
            "inputText": f"Check and correct the below text grammar: ",
            "textGenerationConfig": {
                "temperature": 0,  
                "topP": 0.9,
                "maxTokenCount": 1000,
                "stopSequences": []
            }
        }

        response = client.invoke_model(
            body=body, 
            modelId="amazon.titan-text-express-v1",
            accept='application/json',
            contentType='application/json'
        )
        print(f"response = {response}")

        response_body = json.loads(response.get("body").read())
        print(f"response_body = {response_body}")

        response_body_error = response_body.get("error")
        print(f"response_body_error = {response_body_error}")

        if not response_body_error and response_body_error is None:
            result = response_body
        else:
            raise RuntimeError(f"response_body_error = {response_body_error}")
        
    except Exception as e:
        print(f"correct_grammar error = {e}")
    
    return result