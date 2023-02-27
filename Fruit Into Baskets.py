class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, maxFruits = 0, 0
        fruitMap = {}

        for right in range(len(fruits)):
            fruitMap[fruits[right]] = fruitMap.get(fruits[right], 0) + 1
            while len(fruitMap) > 2:
                fruitMap[fruits[left]] -= 1
                if fruitMap[fruits[left]] == 0:
                    del fruitMap[fruits[left]]
                left += 1
     
            maxFruits = max(maxFruits, right - left + 1)

        return maxFruits
                
        
