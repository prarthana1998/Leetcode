class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        open_count = 0

        for c in s:
            if c == "(":
                open_count += 1
            else:
                if open_count>0:
                    open_count -=1
                
                else:
                    res += 1
        return open_count + res