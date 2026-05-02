import concurrent.futures
def double(n):
    return n * 2


def process_items(items, worker_func):
    """Process items concurrently using a thread pool."""
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(worker_func, items))
    return results
    

if __name__ == "__main__":

    # res = process_items([1, 2, 3], double)  # outputs [2, 4, 6]
    # res = process_items([], double)  # outputs []
    res = process_items(["a", "b"], str.upper)  # outputs ['A', 'B']
    print(res)