# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #  Using extra O(n) space in set()
        # curr = head
        # seen = set()
        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr = curr.next
        # return False
        
        #Using FAST and SLOW pointer - Floyd's Cycle Detection
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False