import time
def calculate(limit):
    """Return the sum of squares from 0 to limit - 1."""
    sqs = [ i * i for i in range(0, limit)]
    sum = 0 
    for el in sqs:
        sum += el
    return sum

def calculate_2(limit):
    """Return the sum of squares from 0 to limit - 1."""
    return sum(i * i for i in range(0, limit))

def find_sums(limits):
    """Apply calculate to each limit and return the results."""
    return [calculate(lim) for lim in limits]

def find_sums_2(limits):
    """Apply calculate to each limit and return the results."""
    return [calculate_2(lim) for lim in limits]
    
if __name__ == "__main__":
    input_list = [1, 5, 10, 285]
    start_1 = time.perf_counter()
    sums = find_sums(input_list)
    elapsed_1 = time.perf_counter() - start_1
    print(f"find_sums: {sums} in {elapsed_1:.2f} seconds")

    start_2 = time.perf_counter()
    sums = find_sums_2(input_list)
    elapsed_2 = time.perf_counter() - start_2
    print(f"find_sums_2: {sums} in {elapsed_2:.2f} seconds")