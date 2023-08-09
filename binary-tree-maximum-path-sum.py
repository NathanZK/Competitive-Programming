# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathSum = 0
        self.dfs(root)
        return self.pathSum

    def dfs(self, root):
        if not root:
            return 0

        maxPath = root.val + max(self.dfs(root.left), self.dfs(root.right))
        currSum = root.val + self.dfs(root.left) + self.dfs(root.right)
        self.pathSum = max(self.pathSum, currSum)

        return maxPath