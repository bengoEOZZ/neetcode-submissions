class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest, streak = 0, 0
        for e in nums:
            if e-1 not in hashSet:
                streak = 1
                while e + streak in hashSet:
                    streak += 1
                longest = max(longest, streak)
        return max(longest, streak)