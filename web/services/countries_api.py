import requests


def countries_api():
    countries = []

    try:
        root_url = "https://restcountries.com/v3.1/all"

        response = requests.get(root_url)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            # print(f"response_json = {response_json}")

            if response_json:
                for item in response_json:
                    country_name = item.get("name").get("common")
                    if country_name:
                        countries.append(country_name)
    except Exception as e:
        print(f"countries_api error = {e}")

    return countries
