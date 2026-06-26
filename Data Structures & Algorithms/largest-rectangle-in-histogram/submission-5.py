class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        maxArea = 0
        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                prevIndex, prevHeight = stack.pop()
                prevArea = prevHeight*(i-prevIndex)
                maxArea = max(maxArea, prevArea)
                start = prevIndex
            stack.append((start, height))
        return maxArea