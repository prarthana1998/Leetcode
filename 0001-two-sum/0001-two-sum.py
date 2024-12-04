class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       numsMap={}
       n = len(nums)
       for i in range(n):
        key = target - nums[i]
        if key in numsMap:
            return[numsMap[key], i]
        numsMap[nums[i]] = i
       return[]
    