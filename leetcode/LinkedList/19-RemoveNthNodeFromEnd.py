
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head

        while curr:
            N += 1
            curr = curr.next

        indexRemove = N - n

        if indexRemove == 0:
            return head.next
        
        curr = head
        for i in range(N - 1):
            if (i + 1) == indexRemove:
                curr.next = curr.next.next
            curr = curr.next
        
        return head

        