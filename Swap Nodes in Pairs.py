# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        forw = head.next
        while forw:
            curr.val, forw.val = forw.val, curr.val
            curr = curr.next.next
            if forw.next == None: break
            forw = forw.next.next
        
        return head
