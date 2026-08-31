class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1][-1]]:
                prev_i = stack.pop()[-1]
                result[prev_i] = i - prev_i
            stack.append([temp, i])

        return result

            
            


        