# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        size = 1
        curr, tail = head, None
        while curr.next:
            size += 1
            curr = curr.next

        tail = curr
        k = k % size
        pos = size - k
        curr = head

        if k == 0:
            return head

        for _ in range(pos-1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        tail.next = head

        return newHead
