# Stack (LIFO)  data structure implementation using python
# Problem 1:
# * Reverse a string

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

    def reverse_string(self, string):
        for index in range(len(string)):
            self.push(string[index])
        rstr = ''
        while self.size() != 0:
            rstr += self.pop()

        return rstr


if __name__ == '__main__':
    # print(dir(Stack))
    st = Stack()
    given_string = "We will conquer COVID-19"
    (print(st.reverse_string(given_string)))
