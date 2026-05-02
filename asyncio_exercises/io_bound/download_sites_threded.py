import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()

    return thread_local.session


def download_site(url):
    session = get_session()

    with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        # print(f"{indicator} - {response.status_code}")
        print(indicator, sep='', end='', flush=True)


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

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
    print(f"\nDownloaded {len(sites)} sites in {end - start:.2f} seconds.")
