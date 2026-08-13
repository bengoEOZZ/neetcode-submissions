class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSequence = 0
        numsSet = set(nums)
        for n in nums:
            if (n-1) not in numsSet:
                length = 1
                while n + length in numsSet:
                    length += 1
                maxSequence = max(maxSequence, length)
        return maxSequence