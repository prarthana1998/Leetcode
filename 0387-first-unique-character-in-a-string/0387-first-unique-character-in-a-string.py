class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_char = Counter(s)

        for i in range(len(s)):
            if unique_char[s[i]] == 1:
                return i

        return -1
            
        