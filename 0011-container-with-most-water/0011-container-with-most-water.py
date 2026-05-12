class Solution:
    def maxArea(self, height: List[int]) -> int:
      max_area, area = 0, 0
      left = 0
      width = 0
      right = len(height) - 1
      while left < right:
        heights = min(height[left], height[right])
        width = right - left
        area = heights * width
        max_area = max(area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

      return max_area