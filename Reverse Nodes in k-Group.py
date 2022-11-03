# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        stack = []
        count = 0
        while head:
            stack.append(head)
            count += 1
            if count == k:
                l, r = 0, k - 1
                while l < r:
                    stack[l].val, stack[r].val = stack[r].val, stack[l].val
                    l += 1
                    r -= 1
                count = 0
                stack = []
            head = head.next
        
        return temp
        
