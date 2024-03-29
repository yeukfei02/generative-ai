import boto3
import json


def handler(event, context):
    print(f"event = {event}")

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "output_text": ""
        })
    }

    if event:
        if event["queryStringParameters"]:
            input = event["queryStringParameters"]["input"]
            if input:
                output_text = generate_text_in_bedrock(input)
                response = {
                    "statusCode": 200,
                    "body": json.dumps({
                        "output_text": output_text
                    })
                }

    print(f"response = {response}")
    return response


def generate_text_in_bedrock(input):
    result = ""

    try:
        client = boto3.client(service_name='bedrock-runtime')

        body = json.dumps({
            "inputText": f"Check, format and correct the grammar of the following text: {input}",
            "textGenerationConfig": {
                "temperature": 0,
                "topP": 0.9,
                "maxTokenCount": 2000,
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
                for item in results:
                    output_text = item["outputText"]
                    result += output_text
        else:
            raise RuntimeError(f"response_body_error = {response_body_error}")

    except Exception as e:
        print(f"generate_text_in_bedrock error = {e}")

    return result
