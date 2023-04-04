class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        cardGcd = count[deck[0]]
        for val in count.values():
            cardGcd = self.gcd(cardGcd, val)

        if cardGcd == 1:
            return False

        return True

    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a%b)
