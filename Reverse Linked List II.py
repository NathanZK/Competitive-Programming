# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        curr.next = head

        for count in range(right):
            if count == left - 1:
                start = curr
            curr = curr.next

        end = curr.next
        curr.next = None

        front, tail = self.reverseList(start.next)
        start.next, tail.next = front, end

        return dummy.next
   
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
        
        return prev, head
        
