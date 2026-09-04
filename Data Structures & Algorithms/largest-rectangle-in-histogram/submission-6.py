class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                prevH, prevI = stack.pop()
                maxArea = max(maxArea, prevH*(i-prevI))
                start = prevI
            stack.append((h, start))
        return maxArea