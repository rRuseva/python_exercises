# io_bound/race.py
from concurrent.futures import ThreadPoolExecutor
from time import sleep
counter = 0

def change_counter(amount):
    global counter
    local_copy = counter   # pretend this is fetched
    sleep(0.05)
    local_copy += amount
    counter = local_copy   # pretend this is sent

def race(num_threads):
    global counter
    counter = 0
    data = [-1 if x %2 else 1 for x in range(50)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(change_counter, data)

    print(counter)
