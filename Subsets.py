class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        possibleSubsets = [[]]

        def dfs(index, curr, possibleSubsets):
            if index == len(nums):
                return
                
            curr.append(nums[index])
            possibleSubsets.append(curr)

            for i in range(index, len(nums)):
                dfs(i+1, curr.copy(), possibleSubsets)

        for i in range(len(nums)):
            dfs(i, [], possibleSubsets)

        return possibleSubsets
