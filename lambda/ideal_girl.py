import boto3
import json
import io
from random import randrange
import base64
from PIL import Image

def handler(event, context):
    print(f"event = {event}")

    response = None

    if event:
        response = get_ideal_girl_in_bedrock(event)
        if response:
            image = Image.open(io.BytesIO(response))
            print(f"image = {image}")

            response = image

            image.show()

    return response

def get_ideal_girl_in_bedrock(event):
    result = None

    try:
        client = boto3.client(service_name='bedrock-runtime')

        # random_seed = get_random_seed()
        # print(f"random_seed = {random_seed}")

        body = {
            "text_prompts": [
                {
                    "text": "",
                    "weight": 0
                }
            ],
            "width": 896,
            "height": 1152,
            "seed": 0,
            "steps": 50,
            # "style_preset": ""
        }

        response = client.invoke_model(
            body=body, 
            modelId="stability.stable-diffusion-xl-v1",
            accept='application/json',
            contentType='application/json'
        )
        print(f"response = {response}")

        response_body = json.loads(response.get("body").read())
        print(f"response_body = {response_body}")

        response_body_result = response_body['result']
        print(f"response_body_result = {response_body_result}")

        base64_image = response_body.get("artifacts")[0].get("base64")
        base64_bytes = base64_image.encode('ascii')
        image_bytes = base64.b64decode(base64_bytes)
        print(f"image_bytes = {image_bytes}")

        finish_reason = response_body.get("artifacts")[0].get("finishReason")

        if finish_reason == 'ERROR' or finish_reason == 'CONTENT_FILTERED':
            raise RuntimeError(f"response_body_error = {finish_reason}")
        else:
            result = image_bytes
        
    except Exception as e:
        print(f"get_ideal_girl_in_bedrock error = {e}")
    
    return result

def get_random_seed():
    random_seed = randrange(100)
    return random_seed