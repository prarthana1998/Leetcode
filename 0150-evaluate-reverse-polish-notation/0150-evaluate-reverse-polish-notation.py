class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for nums in tokens:
            if nums == "+":
                stack.append(stack.pop()+ stack.pop())
            elif nums == "*":
                stack.append(stack.pop()* stack.pop())
            elif nums == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif nums == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b/a)))
            else:
                stack.append(int(nums))
        return stack[-1]
