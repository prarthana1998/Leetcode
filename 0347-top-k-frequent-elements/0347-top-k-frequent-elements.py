class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num]+=1
            else:
                hashMap[num]=1
                # Extract items and sort by frequency
            
        sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        top_k = [item[0] for item in sorted_items[:k]]

        return top_k