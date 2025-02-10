class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Hashmap = {")": "(", "]": "[","}": "{"}

        for i in s:
            if i in Hashmap:
                if stack and stack[-1] == Hashmap[i]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)

        return True if not stack else False