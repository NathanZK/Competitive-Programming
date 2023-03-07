class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        return self.row(k)

    def row(self, k):
        if k == 1:
            return 0

        if k % 2 == 0:
            return 1 - self.row(math.ceil(k/2))

        return self.row(math.ceil(k/2))

