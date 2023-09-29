class WordDictionary:

    def __init__(self):
        self.root = TrieNode()       

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()

            curr = curr.children[w]

        curr.is_end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        return self.searchTrie(word, curr,0)

    def searchTrie(self, word, node, index):
        if index == len(word):
            return node.is_end

        word_exist = False
        if word[index] == ".":
            for child in node.children:
                word_exist = word_exist or self.searchTrie(word,node.children[child],index+1)

        elif word[index] in node.children:
            word_exist = self.searchTrie(word,node.children[word[index]],index+1)

        return word_exist
        
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)