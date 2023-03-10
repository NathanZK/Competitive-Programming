class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        possible = []
        
        for num in range(1, n + 1):
            self.combinations(num, k, [], possible, n+1)

        return possible

    def combinations(self, currNum, k, curr, total, n):
        if currNum > n - k + 1:
            return

        curr.append(currNum)
        if len(curr) == k:
            total.append(curr)
            return

        for num in range(currNum+1, n):
            self.combinations(num, k, curr.copy(), total, n)


