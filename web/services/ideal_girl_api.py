import requests

def ideal_girl_api(input, style_preset):
    result = None

    try:
        root_url = "https://ev6tfvtw2g.execute-api.us-east-1.amazonaws.com/prod"

        params = {
            "input": input
        }

        if style_preset:
            params["style_preset"] = style_preset

        response = requests.get(f"{root_url}/generative-ai/ideal-girl", params=params)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                base64_image = response_json["base64_image"]
                if base64_image:
                    result = base64_image
    except Exception as e:
        print(f"ideal_girl_api error = {e}")

    return result