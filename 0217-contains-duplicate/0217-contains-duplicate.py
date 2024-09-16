class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        n = len(nums)
        for num in nums:
           if num in numMap and numMap[num]>=1:
            return True
           numMap[num] = numMap.get(num, 0) + 1
        return False
        