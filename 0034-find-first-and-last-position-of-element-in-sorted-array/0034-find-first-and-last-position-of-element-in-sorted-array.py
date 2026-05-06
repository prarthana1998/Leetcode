class Solution:
    '''
    [5,7,7,8,8,10] t = 8
    '''
    



    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        first = self.binarysearch(nums, target, True)
        last = self.binarysearch(nums, target, False)
        return [first, last]

    def binarysearch(self,arr, target, firstoccur):
        left, right  = 0, len(arr) - 1
        spot = -1
        while left<=right:
            mid = left + (right-left)//2
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                spot = mid
                if firstoccur:
                    
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return spot
        