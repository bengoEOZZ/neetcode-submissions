class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            length = r-l
            if heights[l] <= heights[r]:
                maxArea = max(maxArea, heights[l]*length)
                l += 1
            else:
                maxArea = max(maxArea, heights[r]*length)
                r -= 1
        return maxArea