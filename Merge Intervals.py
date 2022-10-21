class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        left, right = 0, 1
        intervals = sorted(intervals, key = lambda x: x[0])
        while right < len(intervals):
            if intervals[left][1] >= intervals[right][0]:
                intervals[left][1] = max(intervals[left][1], intervals[right][1])
                intervals.pop(right)
            else:
                left += 1
                right += 1
        return intervals
