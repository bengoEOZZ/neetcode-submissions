class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSorted = nums
        numsSorted.sort()
        if len(nums) < 1:
            return 0
        longestCon, streak = 0, 1
        for i in range(1, len(numsSorted)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                streak += 1
            else:
                longestCon = max(longestCon, streak)
                streak = 1
        return max(longestCon, streak)