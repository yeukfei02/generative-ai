import boto3
import json

def handler(event, context):
    print(f"event = {event}")

    response = None

    if event:
        response = get_correct_grammar_in_bedrock(event)

    return response

def get_correct_grammar_in_bedrock(event):
    result = None

    try:
        client = boto3.client(service_name='bedrock-runtime')

        body = {
            "inputText": f"Check and correct the grammar of the below text or sentence or paragraph: ",
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

        if not response_body_error:
            result = response_body
        else:
            raise RuntimeError(f"response_body_error = {response_body_error}")
        
    except Exception as e:
        print(f"get_correct_grammar_in_bedrock error = {e}")
    
    return result