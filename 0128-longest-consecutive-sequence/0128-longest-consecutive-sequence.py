class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        count = 1
        max_count = -1
        for i in range(n-1):
            if nums[i+1] == nums[i] + 1:
                count+=1
            elif nums[i+1] == nums[i]:
                max_count = max(max_count, count)
                continue
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count
            
        