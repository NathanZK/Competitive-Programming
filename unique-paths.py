class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        squares = (m+n-2)
        n -= 1
        m -= 1
        paths = 1

        while squares > max(m, n):
            paths *= squares
            squares -= 1

        _min = min(n, m)
        while _min > 1:
            paths /= _min
            _min -= 1

        return int(paths)