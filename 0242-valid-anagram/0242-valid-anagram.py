class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numsMap = defaultdict(int)
        for strs in s:
            numsMap[strs]+=1
        for strs in t:
            numsMap[strs]-=1
        
        for val in numsMap.values():
            if val!=0:
                return False
        return True
        