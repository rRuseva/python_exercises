import queue
from codetiming import Timer
import asyncio
import aiohttp


async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.2f}} seconds")
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f"Task {name} getting URL: {url}")
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()


async def main():
    work_queue = asyncio.Queue()
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]

    for url in urls:
        await work_queue.put(url)

    with Timer(text="\nTotal elapsed time: {:.2f}"):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue))
        )


if __name__ == "__main__":
    asyncio.run(main())
