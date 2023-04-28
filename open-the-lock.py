class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        queue = deque([[[0,0,0,0], 0]])

        if "0000" in deadends:
            return -1

        while queue:
            wheel, turns = queue.popleft()
            ans = "".join([str(n) for n in wheel])

            if ans == target:
                return turns

            for i in range(4):
                dec = wheel[:]
                dec[i] = (wheel[i] - 1)% 10
                ans = "".join([str(n) for n in dec])
                if ans not in visited:
                    queue.append([dec, turns + 1])
                    visited.add(ans)

                inc = wheel[:]
                inc[i] = (wheel[i] + 1) % 10
                ans = "".join([str(n) for n in inc])
                if ans not in visited:
                    queue.append([inc, turns + 1])
                    visited.add(ans)

        return -1