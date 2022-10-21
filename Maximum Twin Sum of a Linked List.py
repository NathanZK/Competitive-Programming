# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        numList = []
        sum = 0
        highest = 0
        while head:
            numList.append(head.val)
            head = head.next
        print(numList)
        i = 0
        j = len(numList) - 1
        while i < j:
            sum = numList[i] + numList[j]
            if sum > highest:
                highest = sum
            i += 1
            j -= 1
        return highest
