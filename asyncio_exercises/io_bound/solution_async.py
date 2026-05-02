import asyncio


async def square(n):
    """Return the square of n."""
    return n * n


async def gather_squares(numbers):
    """Square all numbers concurrently and return results."""
    tasks = [asyncio.ensure_future(square(n)) for n in numbers]
    return await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":

    result = asyncio.run(gather_squares([1, 2, 3, 4, 5]))
    print(result)
