
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lengthOfList = 0
        curr = head

        while curr:
            lengthOfList += 1
            curr = curr.next

        
        indexRemove = lengthOfList // 2
        if indexRemove == 0:
            return head.next

        curr = head
        for i in range(lengthOfList - 1):
            if (i + 1) == indexRemove:
                curr.next = curr.next.next
            curr = curr.next
        
        return head