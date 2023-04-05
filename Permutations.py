class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def dfs(arr, bit):
            if len(arr) == len(nums):
                permutations.append(arr[:])
                return
            
            mask = 1
            for i, num in enumerate(nums):
                mask <<= 1
                if bit&(mask):
                    continue

                arr.append(num)
                bit ^= (mask)
                dfs(arr, bit)

                arr.pop()
                bit ^= (mask)
 
        dfs([], 0)
        return permutations
