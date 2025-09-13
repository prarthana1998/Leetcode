class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        dict => key: numbers, value: index
        traverse the dict
        check
        1) if target - key exists in the dict
        s1: present return the indices 
        s2: present return add it to the dict
        2, 7, 11, 15
        0  1.  2.  3 target = 9 
        dict = {2:0, }
        '''

        number_dict = {}
        for i, num in enumerate(nums):
            if target-nums[i] in number_dict:
                return [number_dict[target-nums[i]], i]
            number_dict[nums[i]] = i
        return {}
 