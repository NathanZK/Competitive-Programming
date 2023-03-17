# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        index = 0
        curr = head

        while curr:
            nodes.append(curr)
            curVal = curr.val
            pos = index - 1
            while pos >= 0 and curVal < nodes[pos].val:
                nodes[pos+1].val = nodes[pos].val
                pos -= 1

            nodes[pos+1].val = curVal
            index += 1
            curr = curr.next

        return head


        
