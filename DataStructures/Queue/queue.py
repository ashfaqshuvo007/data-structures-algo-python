# Queue (FIFO) data structure implementation
# lists can be used but not recommended . Use deque() built in collections class in python

from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, element):
        self.buffer.appendleft(element)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0


if __name__ == '__main__':
    q = Queue()
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })

    print(q.dequeue())
