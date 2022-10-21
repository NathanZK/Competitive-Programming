# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        while head and head.next:
            if head.val == head.next.val:
                while head.val == head.next.val:
                    if head.next.next:
                        head = head.next
                    else:
                        head.next = None
                        break
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
