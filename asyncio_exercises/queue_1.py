import queue


def task_1(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} running")
            for x in range(count):
                total += 1
            print(f"Task {name} total: {total}")


def task_2(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")


def main_2():
    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task_2("One", work_queue), task_2("Two", work_queue)]

    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


def mai_1():
    work_queue = queue.Queue()

    for work in [15, 10, 5, 20]:
        work_queue.put(work)

    tasks = [(task, "One", work_queue), (task, "Two", work_queue)]
    for t, n, q in tasks:
        t(n, q)


if __name__ == "__main__":
    # main_1()
    main_2()
