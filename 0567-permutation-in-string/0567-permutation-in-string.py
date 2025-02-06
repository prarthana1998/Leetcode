class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')]+=1
            count_s2[ord(s2[i])-ord('a')]+=1
        #check in s2 with window size of s1, if match yes if no false
        left = 0
        for right in range(len(s2)-len(s1)):
            if count_s1 == count_s2:
                return True
            count_s2[ord(s2[right])-ord('a')]-= 1
            count_s2[ord(s2[right+len(s1)])-ord('a')] +=1

        return count_s1 == count_s2
            
        

                
        