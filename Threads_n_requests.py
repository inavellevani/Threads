import threading
import requests
import json


def get_url(url):
    try:
        response = requests.get(url)
        product_data = response.json()
        with open('data.json', 'a') as outfile:
            json.dump(product_data, outfile, indent=2)
            outfile.write(',\n')

    except Exception:
        return None


def send_requests_in_threads(urlss):
    threads = []
    for url in urlss:
        thread = threading.Thread(target=get_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    base_url = "https://dummyjson.com/products/"
    urls = [f"{base_url}{i}" for i in range(1, 101)]
    url_grouping = [urls[i:i + 20] for i in range(0, len(urls), 20)]
    for group in url_grouping:
        send_requests_in_threads(group)
