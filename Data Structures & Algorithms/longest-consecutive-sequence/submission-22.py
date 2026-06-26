class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for e in numSet:
            if e-1 not in numSet:
                streak = 1
                while e+streak in numSet:
                    streak += 1
                longest = max(longest, streak)
        return longest