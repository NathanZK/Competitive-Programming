class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = min (height[start], height[end]) * (end - start)
            maxArea = max(maxArea, area)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return maxArea
