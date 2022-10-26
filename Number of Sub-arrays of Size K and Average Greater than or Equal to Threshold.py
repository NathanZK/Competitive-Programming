class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        limit = k * threshold
        sum = 0
        for num in arr[0:k]:
            sum += num
        length = 0
        left, right = 0, k - 1
        while right < len(arr):
            if sum >= limit:
                length += 1
            right += 1
            if right == len(arr):
                return length
            sum += arr[right]
            sum -= arr[left]
            left += 1
                
