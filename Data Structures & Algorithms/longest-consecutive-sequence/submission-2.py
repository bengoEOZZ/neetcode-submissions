class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSorted = nums
        numsSorted.sort()
        longestConsecutive = 0
        if len(nums) < 1:
            return longestConsecutive

        currentStreak = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                currentStreak += 1
            else:
                longestConsecutive = max(currentStreak, longestConsecutive)
                currentStreak = 1

        return max(currentStreak, longestConsecutive)