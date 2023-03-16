# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        curr.next = head
        size = 0

        while curr.next:
            size += 1
            curr = curr.next

        curr = dummy
        idx = size - n
        for _ in range(idx):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next
