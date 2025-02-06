class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total_sum = 0

        for ops in operations:

            if ops == 'C':
               total_sum-=stack.pop()

            elif ops == 'D':
                score = stack[-1]*2
                stack.append(score)
                total_sum+=score
            elif ops == '+':
                score = stack[-1]+stack[-2]
                stack.append(score)
                total_sum+=score
            else:
                score = int(ops)
                stack.append(score)
                total_sum+=score

        return total_sum

