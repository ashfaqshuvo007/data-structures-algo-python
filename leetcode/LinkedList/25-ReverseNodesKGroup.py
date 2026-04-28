# Definition for singly-linked list.


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        group = 0

        while curr and group < k:
            curr = curr.next
            group += 1
        
        if group == k:
            curr = self.reverseKGroup(curr, k)

            while group > 0:
                tmp = head.next
                head.next = curr

                curr = head
                head = tmp
                group -= 1
            head = curr

        return head

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    result = solution.reverseKGroup(head, k)

    while result:
        print(result.val)
        result = result.next