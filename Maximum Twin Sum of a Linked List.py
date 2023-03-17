# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twinSum = 0
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = self.reverseList(slow.next)
        slow.next = None

        while list1:
            twinSum = max(twinSum, list1.val + list2.val)
            list1 = list1.next
            list2 = list2.next

        return twinSum

    def reverseList(self, head):
        prev = None
        while head:
            forw = head.next
            head.next = prev
            prev = head
            head = forw

        return prev
