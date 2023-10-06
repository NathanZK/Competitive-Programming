# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.countPaths = 0
        targetMap =  Counter({0:1})
        self.dfs(root, 0, targetSum, targetMap)
        return self.countPaths

    def dfs(self, root, currSum, targetSum, targetMap):
        if not root:
            return 

        currSum += root.val
        complement = currSum - targetSum
        self.countPaths += targetMap[complement]
        targetMap[currSum] += 1

        self.dfs(root.left, currSum, targetSum, targetMap)
        self.dfs(root.right, currSum, targetSum, targetMap)

        targetMap[currSum] -= 1