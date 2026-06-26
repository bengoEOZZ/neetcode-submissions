class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = []
        for i, e in enumerate(nums):
            sortedNums.append((e, i))
        sortedNums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            sumLR = sortedNums[l][0] + sortedNums[r][0]
            if sumLR == target:
                return [min(sortedNums[l][1], sortedNums[r][1]), max(sortedNums[l][1], sortedNums[r][1])]
            elif sumLR < target:
                l += 1
            else:
                r -= 1