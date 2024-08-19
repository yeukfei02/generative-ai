import requests


def best_deal_api(location, timeline):
    result = None

    try:
        root_url = "https://j9pinsyob3.execute-api.us-east-1.amazonaws.com/prod"

        params = {
            "location": location,
            "timeline": timeline
        }

        response = requests.get(
            f"{root_url}/generative-ai/best-deal", params=params)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                output_text = response_json["output_text"]
                if output_text:
                    result = output_text
    except Exception as e:
        print(f"best_deal_api error = {e}")

    return result
