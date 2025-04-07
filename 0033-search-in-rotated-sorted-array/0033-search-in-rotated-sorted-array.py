class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        
        while(low<=high):
            mid = (low + high)//2

           

            if nums[mid]==target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[mid]<target or nums[low]>target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid]>target or nums[high]<target:
                    high = mid - 1
                else:
                    low = mid + 1
                    

        return -1
            
        