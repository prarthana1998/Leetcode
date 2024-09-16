class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        total = n*(n+1) // 2
        actual_sum = sum(nums)
        return total - actual_sum
        