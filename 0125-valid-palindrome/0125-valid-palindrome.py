class Solution:
    def isPalindrome(self, s: str) -> bool:
        #A man, a plan, a canal: Panama
        n = len(s)
        left = 0
        right = n-1
        # check if both are same if not l++ r-- turn into lowercase
        while left<right:
            while left<right and not s[left].isalnum(): left+=1
            while left<right and not s[right].isalnum(): right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
