class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = defaultdict(list)
        self.died = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.died.add(name)

    def getInheritanceOrder(self) -> List[str]:
        inheritanceOrder = []

        def dfs(throne):
            if throne not in self.died:
                inheritanceOrder.append(throne)

            for successor in self.graph[throne]:
                dfs(successor)

        dfs(self.kingName)
        return inheritanceOrder

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()