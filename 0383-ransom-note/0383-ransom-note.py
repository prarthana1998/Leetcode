class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Example 1:

        Input: ransomNote = "a", magazine = "b"
        Output: false
        Example 2:

        Input: ransomNote = "aa", magazine = "ab"
        Output: false
        Example 3:

        Input: ransomNote = "aa", magazine = "aab"
        a:2 b:1
        a:1 b:1
        a:0 b:1
        Output: true

        '''
        magazine_dict = defaultdict(int)

        for num in magazine:
            magazine_dict[num]+=1

        for num in ransomNote:
            magazine_dict[num]-=1
            if magazine_dict[num] < 0:
                return False

        return True

