# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.pathsToRoot(root, "", paths)

        return paths

    def pathsToRoot(self, root, curr, paths):
        if len(curr) != 0:
            curr += "->"+str(root.val)
        else:
            curr += str(root.val)

        if root.left: 
            left = self.pathsToRoot(root.left, curr, paths)
        if root.right:
            right = self.pathsToRoot(root.right, curr, paths)

        if not root.left and not root.right:
            paths.append(curr)
