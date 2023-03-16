class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        incStack = [-1]
        arr.append(0)
        minSum = 0

        for i, num in enumerate(arr):
            while len(incStack) > 1 and num < arr[incStack[-1]]:
                ind = incStack.pop()
                minSum += (arr[ind]*(i-ind)*(ind-incStack[-1]))

            incStack.append(i)

        return minSum % (10**9 + 7)
