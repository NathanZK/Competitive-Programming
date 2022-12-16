class Solution(object):
    def isPalindrome(self, s):
        pal = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                pal += i
        palR = pal[::-1]
        ispal = (pal == palR)
        return ispal
