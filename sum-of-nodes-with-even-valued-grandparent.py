# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(root, parent, grandParent):
            if not root:
                return 0

            evenValued = 0
            if grandParent % 2 == 0:
                evenValued += root.val

            left = dfs(root.left, root.val, parent)
            right = dfs(root.right, root.val, parent)

            return evenValued + left + right
        
        return dfs(root, -1, -1)