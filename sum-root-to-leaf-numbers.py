# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
  
        def dfs(root, num):
            if not root.left and not root.right:
                return 10*num + root.val
            
            num = num*10 + root.val
            total = 0
            if root.left:
                total += dfs(root.left, num)
            
            if root.right:
                total += dfs(root.right, num)

            return total

        return dfs(root, 0)