import requests
import time
import asyncio
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        # print(f"{indicator} - {response.status_code}")
        print(indicator, sep='', end='', flush=True)


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://realpython.com/",
    ] * 80
    print("Start downloading...")
    start = time.perf_counter()
    asyncio.run(download_all_sites(sites))
    end = time.perf_counter()
    print(f"\nDownloaded {len(sites)} sites in {end - start:.2f} seconds.")
