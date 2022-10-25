class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n == 1: return 1
        start = 0
        end = 0
        mx = 0
        hashmap = {}
        while end < n:
            hashmap[fruits[end]] = end
            if len(hashmap) > 2:
                min_val = min(hashmap.values())
                del hashmap[fruits[min_val]]
                start = min_val + 1
            mx = max(mx, end - start + 1)
            end += 1
        return mx
