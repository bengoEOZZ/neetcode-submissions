class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet, longestConsecutive= set(nums), 0
        for e in nums:
            if e-1 not in numsSet:
                currStreak = 1
                while e+currStreak in numsSet:
                    currStreak += 1
                longestConsecutive = max(currStreak, longestConsecutive)
        return longestConsecutive