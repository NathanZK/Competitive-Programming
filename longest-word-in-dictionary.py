class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        currWord = []

        for w in word:
            currWord.append(w)
            if w not in curr.children:
                if len(currWord) == len(word):
                    curr.children[w] = TrieNode()
                    return "".join(currWord)

                return ""
                
            curr = curr.children[w]

        return "".join(currWord)
 
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()
        largest = 0
        longestWord = ""
        
        for word in words:
            newWord = trie.insert(word)
            if len(newWord) > largest:
                largest = len(newWord)
                longestWord = newWord
            elif len(newWord) == largest:
                longestWord = min(longestWord, newWord)


        return longestWord

        

        return 0