class Stack:

    def __init__(self):
        print("creating new stack")
        self.stack = []

    def init_from_list(self, li):
        self.stack[:] = li
        # for item in li:
        #     self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        self.stack = self.stack[:-1]
        return self.stack

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def init_from_list(self, li):
        self.queue[:] = li

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None

        self.queue[:] = self.queue[1:]
        return self.queue

    def size(self):
        return len(self.queue)

    def print_queue(self):
        print(self.queue)


my_list = [1, 2, 3, 4, 5]

print('list:', id(my_list))
print(my_list)

my_stack = Stack()
my_stack.init_from_list(my_list)

print('stack:', id(my_stack), my_stack.size())
my_stack.print_stack()

my_stack.pop()
print('stack:', id(my_stack), my_stack.size())
my_stack.print_stack()

my_queue = Queue()
my_queue.init_from_list(my_list)

print('queue:', id(my_queue))
print(my_queue.size())
my_queue.print_queue()

my_queue.dequeue()

print('queue:', id(my_queue))
print(my_queue.size())
my_queue.print_queue()

