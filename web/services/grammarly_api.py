import requests

def grammarly_api(input):
    result = None

    try:
        root_url = "https://ii5m356p5f.execute-api.us-east-1.amazonaws.com/prod"

        params = {
            "input": input
        }

        response = requests.get(f"{root_url}/generative-ai/grammarly", params=params)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                output_text = response_json["output_text"]
                if output_text:
                    result = output_text
    except Exception as e:
        print(f"grammarly_api error = {e}")

    return result