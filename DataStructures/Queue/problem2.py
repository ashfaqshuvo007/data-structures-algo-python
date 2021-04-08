# Queue (FIFO) data structure implementation
# lists can be used but not recommended . Use deque() built in collections class in python
# Problem:
#  i.  Add a front method in Queue class to get the first number
#  ii. For a given range of numbers ,generate binary  numbers  for them


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

    def front(self):
        return self.buffer[-1]


def produce_binary_numbers(que, n):
    que.enqueue("1")
    for i in range(n):
        start = que.front()
        print(" ", start)
        que.enqueue(start + "0")
        que.enqueue(start + "1")

        que.dequeue()


if __name__ == '__main__':
    q = Queue()
    produce_binary_numbers(q, 10)
