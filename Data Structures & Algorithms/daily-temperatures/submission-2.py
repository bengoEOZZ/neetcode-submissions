class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                smallerTemp, smallerIndex = stack.pop()
                ans[smallerIndex] = i-smallerIndex
            stack.append((temp, i))
        return ans