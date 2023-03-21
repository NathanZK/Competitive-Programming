# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def insertVal(root, val):
            if not root:
                return TreeNode(val)

            if val > root.val:
                root.right = insertVal(root.right, val)

            if val < root.val:
                root.left = insertVal(root.left, val) 

            return root

        for i in range(1, len(preorder)):
            insertVal(root, preorder[i])

        return root
