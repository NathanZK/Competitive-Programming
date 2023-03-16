class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minLength = float("inf")
        left, currSum = 0, 0
        incDeque = deque()

        for right in range(len(nums)):
            currSum += nums[right]
            if currSum >= k:
                minLength = min(minLength, right - left + 1)

            while incDeque and currSum <= incDeque[-1][1]:
                incDeque.pop()

            while incDeque and currSum - incDeque[0][1] >= k:
                ind, val = incDeque.popleft()
                minLength = min(minLength, right - ind)

            incDeque.append([right, currSum])

        if minLength == float("inf"):
            return -1

        return minLength

