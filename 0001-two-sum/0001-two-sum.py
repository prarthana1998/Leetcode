class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for num in range(len(nums)):
            # if target-number present return indices else add
            
            res = target-nums[num]
            if res in numsMap:
                return [numsMap[res],num]
            numsMap[nums[num]] = num
        return {}
        