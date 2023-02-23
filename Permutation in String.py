class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        countS2 = Counter(s2[:len(s1)])
        left, right = 0, len(s1) - 1
        while right < len(s2):
            if countS2 == countS1:
                return True

            right += 1
            if right == len(s2):
                return False
            countS2[s2[right]] = countS2.get(s2[right], 0) + 1
            countS2[s2[left]] -= 1
            if countS2[s2[left]] == 0:
                del countS2[s2[left]]
            left += 1

        return False
            
       
                    
                
        
