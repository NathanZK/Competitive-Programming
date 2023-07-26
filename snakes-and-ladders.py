class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set([1])
        queue = deque([1])
        level = 0
        
        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()
                if curr == n*n:
                    return level

                for i in range(curr+1, min(curr + 6, n*n)+1):
                    nextR, nextC = self.determinePosition(i, n)
                    nextVal = board[nextR][nextC]
                    nextLoc = i
                    if nextVal != -1:
                        nextLoc = nextVal
                    
                    if nextLoc not in visited:
                        queue.append(nextLoc)
                        visited.add(nextLoc)

            level += 1

        return -1

    def determinePosition(self, num, n):
        row = math.ceil(num/n)
        col = num % n

        if row % 2 == 0:
            if col != 0:
                col = n - col
        else:
            if col == 0:
                col = n - 1
            else:
                col -= 1

        return (n-row, col)