import requests

def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()

        return f"{data.get('city')}, {data.get('region')}, {data.get('country')}"
    except requests.RequestException as e:
        print(f"Error getting location: {e}")
        return None
    