'''
dictionary key: word value: list of anagrams
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            group_dict[sorted_word].append(word)  

        return list(group_dict.values())       


       