import requests
from time import sleep

def download_urls(urls):
    results = []
    for url in urls:
        for attempt in range(3):
            try:
                response = requests.get(url)
                response.raise_for_status()
                results.append(response.content)
                break
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt + 1} for {url} failed with error: {e}")
                sleep(1)
        else:
            results.append(None)
    return results

urls = ["https://example.com", "https://nonexistent.url"]
contents = download_urls(urls)
for content in contents:
    print(content)
