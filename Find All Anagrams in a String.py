class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = Counter(p)
        countS = Counter(s[:len(p)])
        left, right = 0, len(p) - 1
        anagrams = []
        while right < len(s):
            if countP == countS:
                anagrams.append(left)
            
            if right == len(s) - 1:
                return anagrams
            right += 1
            countS[s[right]] = countS.get(s[right], 0) + 1
            if countS[s[left]] == 1:
                del countS[s[left]]
            else:
                countS[s[left]] -= 1
            left += 1
            

        return anagrams
            


        
    
