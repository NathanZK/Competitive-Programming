class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.hashmap = {}
        
    def insert(self, key: str, val: int) -> None:
        diff = val
        if key in self.hashmap:
            diff = val - self.hashmap[key]

        self.hashmap[key] = val

        curr = self.root
        for k in key:
            if k not in curr.children:
                curr.children[k] = [diff, TrieNode()]
            else:
                curr.children[k][0] += diff

            curr = curr.children[k][1]

    def sum(self, prefix: str) -> int:
        curr = self.root
        lastSum = 0

        for w in prefix:
            if w not in curr.children:
                return 0

            lastSum = curr.children[w][0]
            curr = curr.children[w][1]

        return lastSum

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)