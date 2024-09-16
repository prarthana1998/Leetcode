class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0,1,0,3,12
        lastNonZeroElement = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[lastNonZeroElement], nums[i] = nums[i], nums[lastNonZeroElement]
                lastNonZeroElement+=1
           