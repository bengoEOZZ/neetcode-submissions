class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 1:
            return 0
        longest, streak = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                streak += 1
            else:
                longest = max(longest, streak)
                streak = 1
        return max(longest, streak)