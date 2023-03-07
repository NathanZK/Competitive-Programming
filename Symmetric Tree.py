# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isEqual(root.left, root.right)

    def isEqual(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True

        if not leftRoot or not rightRoot:
            return False
        
        if leftRoot.val != rightRoot.val:
            return False

        return self.isEqual(leftRoot.left, rightRoot.right) and self.isEqual(leftRoot.right, rightRoot.left)
