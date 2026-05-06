class Solution:
    '''
    [5,7,7,8,8,10] t = 8
    '''
    def firstcoccurance(self,arr, target):
        left, right  = 0, len(arr) - 1
        first = -1
        while left<=right:
            mid = left + (right-left)//2
            if arr[mid] == target:
                first = mid
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return first

    def lastoccurance(self,arr, target):
        left, right  = 0, len(arr) - 1
        last = -1
        while left<=right:
            mid = left + (right-left)//2
            if arr[mid] == target:
                last = mid
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        first = self.firstcoccurance(nums, target)
        last = self.lastoccurance(nums, target)
        return [first, last]
        