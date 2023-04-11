# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.preorder(root)
    
    def preorder(self, root):
        if not root:
            return

        left = self.preorder(root.left)
        right = self.preorder(root.right)

        string = str(root.val)
        if left and not right:
            string += "(" + str(left) + ")"
        if not left and right:
            string += ("()") + "(" + str(right) + ")"
        elif left and right:
            string += "(" + str(left) + ")" + "(" + str(right) + ")"

        return string