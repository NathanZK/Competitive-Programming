# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        data = []
        self.width(root, 0, 0, data)
        maxWidth = 0

        for d in data:
            maxWidth = max(maxWidth, d[1] - d[0] + 1)

        return maxWidth

    def width(self, root, level, elem, data):
        
        if not root:
            return 

        while level >= len(data):
            data.append([])

        if data[level] == []:
            data[level] = [elem, elem]
        else:
            data[level] = [min(elem, data[level][0]), max(elem, data[level][1])]

        left = self.width(root.left, level+1, 2 * elem, data)
        right = self.width(root.right, level+1, 2 * elem + 1, data)