# Stack (LIFO)  data structure implementation using python

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if len(self.container) == 0:
            return "Stack is empty"
        return "False"

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    print(dir(Stack))

