# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = self.inorderTraversal(root)
        count = {}
        maxCount = 0
        modes = []

        for val in stack:
            count[val] = count.get(val, 0) + 1
            maxCount = max(maxCount, count[val])

        for k, v in count.items():
            if v == maxCount:
                modes.append(k)

        return modes


    def inorderTraversal(self, root):
        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right
        
