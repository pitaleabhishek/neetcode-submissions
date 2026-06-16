class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_i = stack.pop()
                temp_result = i-stack_i
                res[stack_i] = (temp_result)
            stack.append((t, i))

        return res