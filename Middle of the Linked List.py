# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        begin = head
        middle = head
        count = 0
        while head:
            count += 1
            head = head .next
        half = count // 2
        head = begin
        count = 0
        while head:
            if count == half:
                middle = head
                break
            count += 1
            head = head.next
        return middle
