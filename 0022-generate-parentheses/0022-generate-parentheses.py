class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        ans = []

        def count(openN, closeN):
            if openN == closeN == n:
                ans.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                count(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                count(openN, closeN+1)
                stack.pop()
        count(0,0)
        return ans
        