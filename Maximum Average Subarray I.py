class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        for num in nums[:k]:
            maxSum += num

        currentSum = maxSum
        left, right = 0, k - 1
        while right < len(nums) - 1:
            right += 1
            currentSum += nums[right]
            currentSum -= nums[left]
            left += 1
            maxSum = max(maxSum, currentSum)

        return maxSum/k
