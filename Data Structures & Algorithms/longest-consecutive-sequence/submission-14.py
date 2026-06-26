class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        numsSorted = nums
        numsSorted.sort()
        longest, streak = 0, 1
        for i in range(1, len(numsSorted)):
            if numsSorted[i] == numsSorted[i-1]:
                continue
            if numsSorted[i] == numsSorted[i-1]+1:
                streak += 1
            else:
                longest = max(longest, streak)
                streak = 1
        return max(longest, streak)