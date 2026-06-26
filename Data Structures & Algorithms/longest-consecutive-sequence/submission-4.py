class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet, longestConsecutive= set(nums), 0
        for e in nums:
            if e-1 not in numsSet:
                currentStreak = 1
                currElem = e
                while currElem + 1 in numsSet:
                    currentStreak += 1
                    currElem += 1
                longestConsecutive = max(currentStreak, longestConsecutive)
        return longestConsecutive