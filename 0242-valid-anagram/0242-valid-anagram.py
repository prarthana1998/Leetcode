class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numsMap = defaultdict(int)
        for x in s:
            numsMap[x]+=1
        for x in t:
            numsMap[x]-=1
        for val in numsMap.values():
            if val!=0:
                return False
        return True