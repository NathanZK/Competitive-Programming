# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = [0]
        self.average(root, count)

        return count[0]

    def average(self, root, count):
        if not root:
            return [0,0]

        left = self.average(root.left, count)
        right = self.average(root.right, count)

        totalSum = left[0] + right[0] + root.val
        totalCount = left[1] + right[1] + 1
        average = totalSum//totalCount

        if root.val == average:
            count[0] += 1

        return [totalSum, totalCount]
        
