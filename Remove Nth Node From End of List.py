# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        count = 0
        if not head.next:
            return None
        while head:
            count += 1
            head = head.next
        end = count - n
        count = 0
        head = temp
        if end == 0:
            return head.next
        while head:
            count += 1
            if count == end:
                head.next = head.next.next
            head = head.next
        return temp
