'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

'''

from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
       self.stack.append(val) 

    def pop(self) -> None:
       self.stack.pop() 
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        
if __name__ == '__main__':
    # print(dir(Stack))
    st = MinStack()
    st.push(1);
    st.push(2);
    st.push(0);
    print(st.top())
    # st.getMin(); # return 0
    # st.pop();
    # st.top();    # return 2
    # st.getMin();

'''
NEETCODE SOLUTION

'''

# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         val = min(val, self.minStack[-1] if self.minStack else val)
#         self.minStack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]
