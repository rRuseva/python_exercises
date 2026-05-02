import asyncio


class AsyncRange_iterable:
    def __init__(self, start, end):
        self.data = range(start, end)

    async def __aiter__(self):
        for i in self.data:
            await asyncio.sleep(0.5)
            yield i


class AsyncRange_iterator:
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


async def main():
    iterable = AsyncRange_iterable(0, 5)
    iterator = AsyncRange_iterator(0, 5)
    print(f"{type(iterable)}: {iterable}")
    print(f"{type(iterator)}: {iterator}")
    # async for i in AsyncRange(0, 5):
    #     print(i)

asyncio.run(main())