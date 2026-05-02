from codetiming import Timer
import asyncio


async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.2f}} seconds")
    while not work_queue.empty():
        delay = await work_queue.get()
        print(f"Task {name} running")
        timer.start()
        await asyncio.sleep(delay)
        timer.stop()


async def main():
    work_queue = asyncio.Queue()

    for work in [15, 10, 5, 2]:
        await work_queue.put(work)

    with Timer(text="\nTotal elapsed time: {:.2f} seconds"):
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),
            asyncio.create_task(task("Two", work_queue))
        )


if __name__ == "__main__":
    asyncio.run(main())
