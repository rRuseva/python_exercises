import asyncio
from codetiming import Timer


class AsyncRange_1:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start < self.end:
            await asyncio.sleep(0.5)
            value = self.start
            self.start += 1
            return value
        else:
            raise StopAsyncIteration


class AsyncRange:
    def __init__(self, start, end):
        self.data = range(start, end)

    async def __aiter__(self):
        for i in self.data:
            await asyncio.sleep(0.5)
            yield i


async def main_1():
    with Timer(text="\nTotal elapsed time: {:.8f}"):
        async for i in AsyncRange(0, 5):
            print(i)


async def main():
    with Timer(text="\nTotal elapsed time: {:.8f}"):
        async for i in AsyncRange(0, 5):
            print(i)


if __name__ == "__main__":
    asyncio.run(main_1())
