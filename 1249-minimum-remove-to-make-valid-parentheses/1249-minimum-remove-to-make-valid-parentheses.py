class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        count = 0
        res = []

        for c in s:

            if c == '(':
                res.append(c)
                count += 1
            elif c == ')' and count > 0:
                res.append(c)
                count -= 1
            elif c != ')':
                res.append(c)
        
        filtered = []

        for i in res[::-1]:
            if i == '('and count > 0:
                count -=1
            else:
                filtered.append(i)
        return "".join(reversed(filtered))

