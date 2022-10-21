# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        stack = []
        while head:
            value = head.val
            stack.append(value)
            head = head.next
            
        return stack == stack[::-1]
