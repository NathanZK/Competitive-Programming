# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathSum = float("-inf")
        self.dfs(root)
        return self.pathSum

    def dfs(self, root):
        if not root:
            return 0

        leftPath = self.dfs(root.left)
        rightPath = self.dfs(root.right)

        path1 = root.val + max(leftPath, rightPath)
        path2 = root.val
        currPath = root.val + leftPath + rightPath
        self.pathSum = max(self.pathSum, currPath, path1, path2)

        return max(path1, path2)