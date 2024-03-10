import requests


def get_ideal_girls_api():
    result = None

    try:
        root_url = "https://edw2m22scb.execute-api.us-east-1.amazonaws.com/prod"

        response = requests.get(f"{root_url}/generative-ai/get-ideal-girls")
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                urls = response_json["urls"]
                if urls:
                    result = urls
    except Exception as e:
        print(f"get_ideal_girls_api error = {e}")

    return result
