# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathMap = {0:1}
        targetCount = 0

        def dfs(root, pathMap, runningSum):
            nonlocal targetCount

            if not root:
                return 0

            runningSum += root.val
            diff = runningSum - targetSum
            
            targetCount += pathMap.get(diff, 0)
            pathMap[runningSum] = pathMap.get(runningSum, 0) + 1

            dfs(root.left, pathMap, runningSum)
            dfs(root.right, pathMap, runningSum)

            pathMap[runningSum] = pathMap.get(runningSum, 0) - 1

        dfs(root, pathMap, 0)
        return targetCount
