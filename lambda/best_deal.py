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
            location = event["queryStringParameters"]["location"]
            timeline = event["queryStringParameters"]["timeline"]
            if location and timeline:
                output_text = generate_text_in_bedrock(location, timeline)
                response = {
                    "statusCode": 200,
                    "body": json.dumps({
                        "output_text": output_text
                    })
                }

    print(f"response = {response}")
    return response


def generate_text_in_bedrock(location, timeline):
    result = ""

    try:
        client = boto3.client(service_name='bedrock-runtime')

        body = json.dumps({
            "prompt": f"Generate {location}'s best and hot deals for {timeline}, get data from Google search and extract the insights into bullet points, and create a summary at the end.",
            "temperature": 0.3,
            "top_p": 0.9,
            "max_gen_len": 800,
        })

        response = client.invoke_model(
            body=body,
            modelId="meta.llama3-8b-instruct-v1:0"
        )
        print(f"response = {response}")

        if response:
            response_body = response.get("body")
            if response_body:
                model_response = json.loads(response["body"].read())
                print(f"model_response = {model_response}")

                response_text = model_response.get("generation")
                print(f"response_text = {response_text}")

                result = response_text
    except Exception as e:
        print(f"generate_text_in_bedrock error = {e}")

    return result
