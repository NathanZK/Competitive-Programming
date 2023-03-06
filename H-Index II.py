class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations[-1] == 0:
            return 0

        left, right = -1, len(citations)
        while left + 1 < right:
            mid = (left + right)//2
            num_rem = len(citations) - mid - 1
            if num_rem >= citations[mid]:
                left = mid
            else:
                right = mid

        return len(citations) - right
