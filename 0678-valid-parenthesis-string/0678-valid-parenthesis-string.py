class Solution:
    def checkValidString(self, s: str) -> bool:
        # if s[i] == '* -> "".(, )
        low, high = 0, 0
        for strs in s:
            if strs == "(":
                low += 1
                high += 1
    
            elif strs == ")":
                low -= 1
                high -= 1
            else:
                high += 1
                low -= 1 
            if high < 0:
                return False
            low = max(low, 0)
        

        return low == 0
        
   