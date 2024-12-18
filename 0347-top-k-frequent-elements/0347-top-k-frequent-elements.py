class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)] # A list that has a list of values each
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        for nums, c in hashMap.items():
            freq[c].append(nums)
        
        res = []
        for i in range(len(freq)-1, 0 , -1):
            for nums in freq[i]:
                res.append(nums)
                if len(res)==k:
                    return res
            
            
