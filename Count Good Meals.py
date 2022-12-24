class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        hashmap = Counter(deliciousness)
        count = 0

        for num in hashmap.keys():
            complement = float('inf')
            if num != 0:
                complement = 2**(int(math.log(num, 2)) + 1) - num
                if math.floor(math.log(num, 2)) == math.log(num,2):
                    count += hashmap.get(0, 0) * hashmap[num]

            if complement in hashmap and complement <= num:
                if complement == num:
                    count += (hashmap[num] * (hashmap[num] - 1))/2
                else:
                    count += (hashmap[num] * hashmap[complement])

        return int(count) % (10**9 + 7)
