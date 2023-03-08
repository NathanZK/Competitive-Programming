# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.check(root, p, q)

    def check(self, root, p, q):
        if root == None:
            return None

        left = self.check(root.left, p, q)
        right = self.check(root.right, p, q)

        curr = None
        if root.val == q.val:
            curr = q

        if root.val == p.val:
            curr = p

        if curr:
            return curr
        if left and right:
            return root
        
        if left or right:
            return left or right
   
 
        return None

  

   

