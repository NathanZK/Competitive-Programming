# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        prev = head
        while head:
            if head.next:
                if head.val == head.next.val:
                    if head == temp:
                        head = head.next
                        temp = head
                        prev = head
                        continue
                    else:
                        prev.next = head.next
                else:
                    prev = head
            head = head.next
    
        return temp
