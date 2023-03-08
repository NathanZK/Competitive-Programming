# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrder = []
        self.order(root, 0, levelOrder)
        return levelOrder
    
    def order(self, root, depth, levelOrder):
        if not root:
            return None

        left = self.order(root.left, depth+1, levelOrder)
        right= self.order(root.right, depth+1, levelOrder)

        while depth >= len(levelOrder):
            levelOrder.append([])

        levelOrder[depth].append(root.val)
