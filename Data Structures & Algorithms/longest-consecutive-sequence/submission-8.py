class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet, longestCon = set(nums), 0
        for e in hashSet:
            if e-1 not in hashSet:
                streak = 1
                while e + streak in hashSet:
                    streak += 1
                longestCon = max(longestCon, streak)
        return longestCon