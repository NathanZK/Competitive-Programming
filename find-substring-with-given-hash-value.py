class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        hashed = 0
        s = s[::-1]
        shift = ord('a') - 1
        powers = [pow(power, (k - i - 1), modulo) for i in range(k)]

        for i in range(k):
            idx = ord(s[i]) - shift
            hashed += idx * powers[i]
            hashed %= modulo

        left, index = 0, 0
        if hashed == hashValue:
            index = left

        for right in range(k, len(s)):
            idxLeft = ord(s[left]) - shift
            hashed -= idxLeft * powers[0]
            hashed %= modulo

            idxRight =  (ord(s[right]) - shift)
            hashed = hashed*power + idxRight
            hashed %= modulo

            left += 1
            if hashed == hashValue:
                index = left

        return s[index:index+k][::-1]