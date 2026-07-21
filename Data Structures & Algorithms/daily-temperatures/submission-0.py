class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            current_temp = temperatures[i]

            while stack and stack[-1][0] <= current_temp:
                stack.pop()

            if stack:
                result[i] = stack[-1][1] - i

            stack.append((current_temp, i))

        return result

