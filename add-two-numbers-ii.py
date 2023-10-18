# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummy = ListNode()
        head = dummy 
        carry = 0

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            curr = num1+num2+carry
            carry = curr //10
            head.next = ListNode(curr%10)
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)
            head = head.next

        return self.reverse(dummy.next)

    def reverse(self, head):
        dummy = None

        prev, curr = dummy, head
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        return prev