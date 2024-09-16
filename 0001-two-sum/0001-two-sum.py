class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap --> check if target - number if present return if not add the number in the map

        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [i, numMap[complement]]
            numMap[nums[i]] = i

        return []


        
        # 2, 7, 11, 15 t=9