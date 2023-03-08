# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        colMap = defaultdict(list)
        self.traverse(root,0, 0, colMap)

        for col in list(colMap.keys()):
            colMap[col] = sorted(colMap[col])

        vertical = sorted(colMap.items())
        
        for _, col in vertical:
            values = []
            for _,val in col:
                values.append(val)

            ans.append(values)        

        return ans

    def traverse(self, root, currRow, currCol, colMap):
        if not root:
            return

        colMap[currCol].append((currRow, root.val))

        self.traverse(root.left, currRow+1, currCol-1, colMap)
        self.traverse(root.right, currRow+1, currCol+1, colMap)


        
