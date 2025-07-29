import requests

def fetch_status(url):
    """
    Fetches the status from the given URL and prints the response.

    Args:
        url (str): The URL to fetch the status from.
    """
    try:
        response = requests.get(url)
        print(f"Response: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    # Fetching from the specified URLs
    fetch_status("https://intranet.hbtn.io/status")
    fetch_status("http://0.0.0.0:5050/status")
