class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
      
       
        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                while length + n in num_set:
                    length +=1
                count = max(length, count)
        return count