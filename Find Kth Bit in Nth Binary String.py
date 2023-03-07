class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.kthBit(n, k))

    def kthBit(self, n, k):
        if n == 1:
            return 0

        elems = 2 ** n
        if k == elems/2:
            return 1

        if k > elems/2:
            return 1 - self.kthBit(n - 1, elems - k)

        return self.kthBit(n - 1, k)
