class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            freq[s[right]]+=1
            max_length = max(freq.values())
            curr_length = right - left + 1

            if curr_length - max_length > k:
                freq[s[left]]-=1
                left+=1
            res = max(res, right - left + 1)
    
        return res