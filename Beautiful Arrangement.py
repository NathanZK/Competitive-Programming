class Solution:
    def countArrangement(self, n: int) -> int:
        beautiful = 0

        def dfs(index, bit, curr):
            nonlocal beautiful

            if curr:
                if max(curr[-1], index) % min(curr[-1], index) != 0:
                    return
                if len(curr) == n:
                    beautiful += 1

            if index == n:
                return

            mask = 1
            for i in range(1, n+1):
                mask <<= 1
                if bit & mask:
                    continue

                curr.append(i)
                bit ^= mask
                dfs(index+1, bit, curr)

                curr.pop()
                bit ^= mask

        dfs(0, 0, [])
        return beautiful
