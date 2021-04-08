# Stack (LIFO)  data structure implementation using python
# Problem 2:
# *Check if a string contains balanced brackets
# Considering "()","{}" and "[]" as balanced
# Check "({a+b})", "))((a+b}{", "((a+b))","))", "[a+b]*(x+2y)*{gg+kk}"

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

    def is_matched(self, ch1, ch2):
        match_dict = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        return match_dict[ch1] == ch2

    def is_balanced(self, string):
        for ch in string:
            if ch == '(' or ch == '{' or ch == '[':
                self.push(ch)
            if ch == ')' or ch == '}' or ch == ']':
                if self.size() == 0:
                    return False
                if not self.is_matched(ch, self.pop()):
                    return False
        return self.size() == 0


if __name__ == '__main__':
    # print(dir(Stack))
    st = Stack()
    print("({a+b}) is balanced: ", st.is_balanced("({a+b})"))
    print("))((a+b}{ is balanced: ", st.is_balanced("))((a+b}{"))
    print("((a+b)) is balanced: ", st.is_balanced("({a+b})"))
    print(")) is balanced: ", st.is_balanced("))"))
    print("[a+b]*(x+2y)*{gg+kk} is balanced: ", st.is_balanced("[a+b]*(x+2y)*{gg+kk}"))
