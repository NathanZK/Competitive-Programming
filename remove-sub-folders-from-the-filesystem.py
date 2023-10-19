class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.folders = []

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]
        curr.is_end = True

    def search(self):
        curr = self.root
        for key in curr.children:
            if key:
                self.dfs(curr.children[key], ["", key])

    def dfs(self, curr, arr):
        if curr.is_end:
            self.folders.append(arr[:])
            return

        for child in curr.children:
            arr.append(child)
            self.dfs(curr.children[child], arr)
            arr.pop()

    def accessFolders(self):
        return self.folders
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for f in folder:
            word = f.split("/")
            trie.insert(word[1:])

        trie.search()
        folders = trie.accessFolders()

        for i in range(len(folders)):
            folders[i] = "/".join(folders[i])

        return folders