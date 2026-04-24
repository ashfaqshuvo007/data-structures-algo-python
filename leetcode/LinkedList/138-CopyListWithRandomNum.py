
from typing import Optional

"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # ===== Approach 1 - Using Hashmap (two pass) ======= #
        oldToCopy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
    

    # ===== Approach 1 - Using Hashmap (One pass) ======= #
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None
        
        curr = head
        while curr:
            oldToCopy[curr].val = curr.val
            oldToCopy[curr].next = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]