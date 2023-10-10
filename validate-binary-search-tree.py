# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        res = self.in_order_traversal(root)
        resS = sorted(res)
        start = 0
        next = 1
        while next < len(resS):
            if resS[start] == resS[next]:
                return False
            start += 1
            next += 1
        return res == resS
    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.val)
            res = res + self.in_order_traversal(root.right)
        return res