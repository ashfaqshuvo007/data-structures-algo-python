
from typing import List


class Solution:
    # def add(self, num1, num2):
    #     return num1 + num2
    # def sub(self,num1, num2):
    #     return (num2) - num1
    # def mul(self,num1, num2):
    #     return num1 * num2
    # def div(self,num1, num2):
    #     if num1 <= 0:
    #         return 0
    #     else:
    #         return num2 / num1
        
    # def decide_operation(self, operation,num1, num2):
    #     switch = {
    #         '+': self.add(num1, num2), 
    #         '-': self.sub(num1,num2), 
    #         '*': self.mul(num1,num2), 
    #         '/': self.div(num1,num2)
    #     }

    #     return switch.get(operation)

    def evalRPN(self, tokens: List[str]) -> int:
        # operators = ['+', '-', '*', '/']
        # stack = []
        # result = 0

        # if len(tokens) < 2:
        #     return int(tokens.pop())

        # for c in tokens:
        #     if c not in operators:
        #         stack.append(c)  # stack = [0,2,-3,]
        #         continue
        #     else:
        #         print(stack)
        #         result = self.decide_operation(c,(int(stack[-1])), (int(stack[-2]))) # (-3) - 2
        #         stack.pop()
        #         stack.pop()
        #         stack.append(result)
        # return int(result)
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    # tokens = ["1","2","+","3","*","4","-"]
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    tokens = ["4","-2","/","2","-3","-","-"]


    print(sol.evalRPN(tokens))
