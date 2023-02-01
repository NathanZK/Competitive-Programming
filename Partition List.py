# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1,dummy2 = ListNode(), ListNode()
        curr1, curr2 = dummy1, dummy2
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next

            head = head.next

        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next
         
