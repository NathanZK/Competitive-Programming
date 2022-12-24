class Solution:
    def average(self, salary: List[int]) -> float:
        Sum = sum(salary) - min(salary) - max(salary)
        return Sum/(len(salary) - 2)
