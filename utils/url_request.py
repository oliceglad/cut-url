import requests

def check_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code
    except requests.RequestException:
        return None
