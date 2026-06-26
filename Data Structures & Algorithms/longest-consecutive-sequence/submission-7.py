class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSorted = nums
        numsSorted.sort()
        if len(nums) < 1:
            return 0
        longestCon, streak = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                streak += 1
            else:
                longestCon = max(streak, longestCon)
                streak = 1
        return max(streak, longestCon)