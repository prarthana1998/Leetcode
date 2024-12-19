class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in count:
                count[sorted_word] = [word]
            else:
                count[sorted_word].append(word)
        ans = []
        for value in count.values():
            ans.append(value)
        return ans
        