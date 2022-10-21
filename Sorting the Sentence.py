class Solution(object):
    def sortSentence(self, s):
        s = s.split()
        sort = ['a' for i in s]
        for word in s:
            pos = int(word[-1]) - 1
            sort[pos] = word[0:len(word) - 1]
        sort =" ".join(sort)
        return sort
