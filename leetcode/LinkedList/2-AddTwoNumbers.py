# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        # To handle case: 0 + 0 + (carry > 0) we need a new node for that carry
        # Hence in the while loop we also check for carry != None
        while l1 or l2 or carry:

            #normalize digits from both lists
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            # Calculate new digit
            total = n1 + n2 + carry

            # get carry oput
            carry = total // 10
            # Create new node in result
            total = total % 10
            curr.next = ListNode(total)

            # Update the pointers
            curr = curr.next
            # checking any of the lists outgrow another
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        