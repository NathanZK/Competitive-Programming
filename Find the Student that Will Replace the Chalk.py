class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum = 0
        for i in chalk:
            sum += i
        k = k % sum
        i = 0
        while True:
            i %= len(chalk)
            if k == 0:
                return i
            elif k - chalk[i] < 0:
                return i
            k -= chalk[i]
            i += 1
