class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sumSkill = skill[0] + skill[-1]
        chemistry = 0
        left, right = 0, len(skill) - 1
        while left < right:
            Sum = skill[left] + skill[right]
            if sumSkill == Sum:
                chemistry += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1

        return chemistry
