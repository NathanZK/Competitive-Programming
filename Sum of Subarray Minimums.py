class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        decStack = [-1]
        arr.append(0)
        minSum = 0

        for i, num in enumerate(arr):
            while len(decStack) > 1 and num < arr[decStack[-1]]:
                ind = decStack.pop()
                minSum += (arr[ind]*(i-ind)*(ind-decStack[-1]))

            decStack.append(i)

        return minSum % (10**9 + 7)
