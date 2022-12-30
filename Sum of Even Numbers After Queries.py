class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        evenSum = 0
        for n in nums:
            if n % 2 == 0:
                evenSum += n

        for val, index in queries:
            if nums[index] % 2 == 0:
                evenSum -= nums[index]
            nums[index] += val
            
            if nums[index] % 2 == 0:
                evenSum += nums[index]
            res.append(evenSum)

        return res

