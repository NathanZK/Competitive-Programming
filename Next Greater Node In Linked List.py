# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        decStack, greaterNode = [], []
        curr, index = head, 0

        while curr:
            while decStack and curr.val > decStack[-1][1]:
                idx, nodeVal = decStack.pop()
                greaterNode[idx] = curr.val

            decStack.append([index, curr.val])
            index += 1
            greaterNode.append(0)
            curr = curr.next

        return greaterNode
            

        
