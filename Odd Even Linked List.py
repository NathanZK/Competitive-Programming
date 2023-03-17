# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(0), ListNode(0)
        oddHead, evenHead = odd, even
        curr = head
        count = 0

        while curr:
            count += 1
            if count % 2 == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next

            curr = curr.next

        even.next = None
        odd.next = evenHead.next

        return oddHead.next
