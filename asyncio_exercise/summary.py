import asyncio
import json
import time
import aiohttp


async def worker(name, n, session):
    print(f"worker-{name}")
    url = f"https://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16"
    response = await session.request(method='GET', url=url)
    value = await response.text()
    # print(f"type of value: {type(value)}, value: {value}")
    if response.status != 200:
        print(f"Error fetching data: {response.status}: {value}")
        return None
    value = json.loads(value)
    return sum(value.get('data', []))


async def main():
    async with aiohttp.ClientSession() as session:
        # response = await worker('bob', 3, session)
        # print(f"response: {response}, type: {type(response)}")
        sums = await asyncio.gather(*(worker(f"w_{i}", n, session) for i, n in enumerate(range(2,5))))
        print(f"sums: {sums=}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed_time = time.perf_counter() - start_time
    print(f'executed in {elapsed_time:.2f} seconds')
