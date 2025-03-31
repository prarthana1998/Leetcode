class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if(nums[0] < nums[len(nums)-1]):
            return nums[0]
        

        while low<high:
            mid = low + (high-low)//2
            if nums[mid]>nums[high]:
                low = mid + 1
            else:
                high=mid
        return nums[low]

        if nums[low] < nums[high]:  # Already sorted, return first element
            return nums[low]

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:  
                low = mid + 1  # Minimum is in the right half
            else:
                high = mid  # Minimum could be at mid

        return nums[low]  # 'low' will be at the minimum