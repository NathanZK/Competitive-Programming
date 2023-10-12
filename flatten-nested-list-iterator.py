# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattenedList = []
        self.idx = -1
        self.iterateList(nestedList)
        
    def next(self) -> int:
        self.idx += 1
        return self.flattenedList[self.idx]
    
    def hasNext(self) -> bool:
        if self.idx < len(self.flattenedList)-1:
            return True

        return False

    def iterateList(self, arr):
        for nest in arr:
            if nest.isInteger():
                self.flattenedList.append(nest.getInteger())
            if nest.getList():
                self.iterateList(nest.getList())

         
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())