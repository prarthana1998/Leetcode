class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #30, 60, 90
        results = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp: #temperature[0]<60
                index = stack.pop()
                results[index] = i-index
            stack.append(i)
        return results

