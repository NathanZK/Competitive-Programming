# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = add = ListNode(0)
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum_ = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            add.next = ListNode(sum_)
            add = add.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            add.next = (ListNode(carry))

        return dummy.next
