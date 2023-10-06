# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        self.dfs(root, [], 0, targetSum, paths)
        return paths

    def dfs(self, node, currPath, currSum, targetSum, paths):
        if not node:
            return None

        currVal = node.val
        currPath.append(currVal)
        currSum += currVal
        left = self.dfs(node.left, currPath[:], currSum, targetSum, paths)
        right = self.dfs(node.right, currPath[:], currSum, targetSum, paths)

        if not node.left and not node.right:
            if currSum == targetSum:
                paths.append(currPath)
                return