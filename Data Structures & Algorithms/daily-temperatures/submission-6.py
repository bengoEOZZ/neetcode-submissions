class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prevIndex, prevHeight = stack.pop()
                ans[prevIndex] = i - prevIndex
            stack.append((i, temp))
        return ans