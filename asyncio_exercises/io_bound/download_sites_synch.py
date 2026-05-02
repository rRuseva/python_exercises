import requests
import time

def get_session():
    return requests.Session()


def download_site(url):
    session = get_session()

    with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        # print(f"{indicator} - {response.status_code}")
        print(indicator, sep='', end='', flush=True)


def download_all_sites(sites):
    for url in sites:
        download_site(url)

    print()


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://realpython.com/",
    ] * 8
    print("Start downloading...")
    start = time.perf_counter()
    download_all_sites(sites=sites)
    end = time.perf_counter()
    print(f"Downloaded {len(sites)} sites in {end - start:.2f} seconds.")
