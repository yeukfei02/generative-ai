import boto3
import json
from random import randrange

def handler(event, context):
    print(f"event = {event}")

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "base64_image": ""
        })
    }

    if event:
        if event["queryStringParameters"]:
            input = event["queryStringParameters"]["input"]
            if input:
                style_preset = event["queryStringParameters"]["style_preset"] if "style_preset" in event["queryStringParameters"] else "photographic"
                base64_image = get_ideal_girl_in_bedrock(input, style_preset)
                if base64_image:
                    response = {
                        "statusCode": 200,
                        "body": json.dumps({
                            "base64_image": base64_image
                        })
                    }

    print(f"response = {response}")
    return response

def get_ideal_girl_in_bedrock(input, style_preset):
    result = None

    try:
        client = boto3.client(service_name='bedrock-runtime')

        # random_seed = get_random_seed()
        # print(f"random_seed = {random_seed}")

        negative_prompts = [
            "out of frame", 
            "close up", 
            "long neck", 
            "blurry", 
            "blurry eyes", 
            "disfigured eyes", 
            "deformed eyes", 
            "abstract", 
            "disfigured", 
            "deformed", 
            "cartoon", 
            "animated", 
            "toy", 
            "figure", 
            "framed", 
            "3d", 
            "out of frame", 
            "hands", 
            "cartoon", 
            "3d", 
            "disfigured", 
            "bad art", 
            "deformed", 
            "deformed feet", 
            "feet misshaped", 
            "poorly drawn", 
            "extra limbs", 
            "close up", 
            "b&w", 
            "weird colors", 
            "blurry", 
            "watermark duplicate", 
            "morbid", 
            "mutilated", 
            "out of frame", 
            "extra feet", 
            "mutated feet", 
            "poorly drawn feet", 
            "poorly drawn toes", 
            "mutation", 
            "deformed", 
            "ugly", 
            "blurry", 
            "bad anatomy", 
            "bad proportions", 
            "extra limbs", 
            "cloned feet", 
            "disfigured", 
            "ugly", 
            "extra limbs", 
            "bad anatomy", 
            "gross proportions", 
            "malformed limbs", 
            "missing arms", 
            "missing legs", 
            "extra arms", 
            "extra legs", 
            "mutated hands", 
            "fused fingers", 
            "too many toes", 
            "blurry", 
            "bad anatomy", 
            "extra limbs", 
            "poorly drawn face", 
            "poorly drawn toes", 
            "missing toes", 
            "mutated feet", 
            "fused toes", 
            "too many toes", 
            "long neck", 
            "blurry", 
            "bad anatomy", 
            "extra limbs", 
            "poorly drawn face", 
            "poorly drawn feet", 
            "missing toes", 
            "ugly toes", 
            "extra toes", 
            "extra legs", 
            "extra arms", 
            "extra hands"
        ]

        body = json.dumps({
            "text_prompts": (
                [{ "text": input, "weight": 1.0 }]
                + [{ "text": negative_prompt, "weight": -1.0 } for negative_prompt in negative_prompts]
            ),
            "width": 896,
            "height": 1152,
            "seed": 0,
            "steps": 50,
            "style_preset": style_preset
        })

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
        # print(f"base64_image = {base64_image}")

        finish_reason = response_body.get("artifacts")[0].get("finishReason")

        if finish_reason == 'ERROR' or finish_reason == 'CONTENT_FILTERED':
            raise RuntimeError(f"response_body_error = {finish_reason}")
        else:
            result = base64_image
        
    except Exception as e:
        print(f"get_ideal_girl_in_bedrock error = {e}")
    
    return result

def get_random_seed():
    random_seed = randrange(100)
    return random_seed