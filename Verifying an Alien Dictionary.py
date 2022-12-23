class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        keyOrder = {}
        for i, char in enumerate(order):
            keyOrder[char] = chr(ord("a") + i)
            
        for n in range(len(words)):
            words[n] = list(words[n])
            for i in range(len(words[n])):
                words[n][i] = keyOrder[words[n][i]]
            words[n] = "".join(words[n])
        
        newWords = sorted(words)
        return newWords == words
