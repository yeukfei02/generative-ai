import boto3
import json

def handler(event, context):
    print(f"event = {event}")

    response = None

    if event:
        if event["queryStringParameters"]:
            input = event["queryStringParameters"]["input"]
            if input:
                response = get_correct_grammar_in_bedrock(input)

    return response

def get_correct_grammar_in_bedrock(input):
    result = None

    try:
        client = boto3.client(service_name='bedrock-runtime')

        body = json.dumps({
            "inputText": f"Check and correct the grammar of the below text: {input}",
            "textGenerationConfig": {
                "temperature": 0,  
                "topP": 0.9,
                "maxTokenCount": 1000,
                "stopSequences": []
            }
        })

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

        if response_body_error is None:
            results = response_body["results"]
            if results:
                outputText = results[0]["outputText"]
                result = outputText
        else:
            raise RuntimeError(f"response_body_error = {response_body_error}")
        
    except Exception as e:
        print(f"get_correct_grammar_in_bedrock error = {e}")
    
    return result