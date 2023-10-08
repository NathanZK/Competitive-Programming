# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # self.commonAncestor = root
        _, commonAncestor = self.dfs(root, p, q)
        return commonAncestor

    def dfs(self, node, p, q):
        if not node:
            return [False, None]

        curr = False
        left, leftAns = self.dfs(node.left, p, q)
        right, rightAns = self.dfs(node.right, p, q)
        currAns = None

        if node == p or node == q:
            curr = True

        if (curr and left) or (curr and right) or (left and right):
            currAns = node

        return [left or right or curr, leftAns or rightAns or currAns]