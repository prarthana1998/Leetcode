class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest_seq = 0

        for num in nums: # 1, 2, 9, 10, 11
            if num-1 not in hash_set:
                current_num = num
                current_seq = 1
                while current_num+1 in hash_set:
                    current_num+=1
                    current_seq+=1
                longest_seq = max(current_seq,longest_seq)
        
        return longest_seq

