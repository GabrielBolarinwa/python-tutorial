import asyncio
import threading
import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def current(self):
        return self.buffer[-1]


food_queue = Queue()

orders = ["pizza", "samosa", "pasta", "biryani", "burger"]


def queue_order():
    for order in orders:
        food_queue.enqueue(order)
        time.sleep(0.5)


def serve_order():
    while True:
        if food_queue.size() > 0:
            print(food_queue.dequeue())
            time.sleep(2)
        else:
            break


thread1 = threading.Thread(target=queue_order)
thread2 = threading.Thread(target=serve_order)
thread1.start()
time.sleep(1)
thread2.start()

binary_queue = Queue()


def print_binary(n):
    binary_queue.enqueue("1")
    for _ in range(n):
        current_number = binary_queue.current()
        print(current_number)
        binary_queue.enqueue(current_number + "0")
        binary_queue.enqueue(current_number + "1")

        binary_queue.dequeue()


print_binary(10)
