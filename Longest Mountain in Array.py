class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        i = 1
        maxM = 0
        while i < len(arr) - 1:
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                count = 1
                left = i
                right = i
                while left > 0 and arr[left - 1] < arr[left]:
                    count += 1
                    left -= 1
                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    count += 1
                    right += 1
                maxM = max(maxM, count)
            i += 1
        return maxM
