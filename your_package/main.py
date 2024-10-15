
import requests

def make_request(url):
    try:
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    make_request("http://example.com")
