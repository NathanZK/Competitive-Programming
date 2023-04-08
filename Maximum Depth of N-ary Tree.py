"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.traverse(root)

    def traverse(self, root):
        if not root:
            return 0

        depth = 0
        for child in root.children:
            childDepth = self.traverse(child)
            depth = max(depth, childDepth)

        return depth + 1
