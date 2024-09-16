class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap --> check if target - number if present return if not add the number in the map

        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement]!=i:
                return [i, numMap[complement]]

        return []


        
        # 2, 7, 11, 15 t=9