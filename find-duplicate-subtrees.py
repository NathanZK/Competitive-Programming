# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.hashNodes = Counter()
        self.duplicates = set()
        self.dfs(root)

        return self.duplicates

    def dfs(self, root):
        if not root:
            return [-1000]

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        currArr = [root.val] + left + right

        if self.hashNodes[tuple(currArr)] == 1:
            self.duplicates.add(root)
            self.hashNodes[tuple(currArr)] += 1
        else:
            self.hashNodes[tuple(currArr)] += 1

        return currArr