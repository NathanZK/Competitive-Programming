class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordBinary = []
        maxVal = 0

        for word in words:
            wordBinary.append(self.convertToBinary(word))

        for i in range(len(wordBinary)):
            for j in range(i+1, len(wordBinary)):
                if wordBinary[i] & wordBinary[j] == 0:
                    maxVal = max(maxVal, len(words[i]) * len(words[j]))

        return maxVal


    def convertToBinary(self, word):
        binary = 0

        for char in word:
            mask = ord(char)-97
            binary |= (1<<mask)
        
        return binary
