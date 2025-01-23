class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in hashSet:
                hashSet.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in hashSet:
                    hashSet.remove(s[left])
                    left+=1
                hashSet.add(s[right])

        return max_length

        