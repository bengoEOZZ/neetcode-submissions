class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0
        heights.append(0)
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                prevHeight, prevIndex = stack.pop()
                prevArea = prevHeight*(i-prevIndex)
                maxArea = max(maxArea, prevArea)
                start = prevIndex
            stack.append((height, start))
        return maxArea