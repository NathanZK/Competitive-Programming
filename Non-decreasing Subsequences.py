class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subSeq = set()

        def dfs(index, arr):
            if arr and nums[index] < arr[-1]:
                return

            arr.append(nums[index])
            if len(arr) >= 2:
                subSeq.add(tuple(arr))

            for i in range(index, len(nums)-1):
                dfs(i+1, arr.copy())

        for i in range(len(nums)):
            dfs(i, [])

        return subSeq
