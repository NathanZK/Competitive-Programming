class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        rightInterval = [-1] * (len(intervals))

        for i in range(len(intervals)):
            intervals[i].append(i)

        intervals.sort()
        for i in range(len(intervals)):
            left, right = i - 1, len(intervals)

            while left + 1 < right:
                mid = (left + right)//2
                start, end, ind = intervals[mid]
                if start < intervals[i][1]:
                    left = mid
                else:
                    right = mid

            if right != len(intervals):
                start, end, ind = intervals[i]
                startR, endR, indR = intervals[right]
                rightInterval[ind] = indR

        return rightInterval
