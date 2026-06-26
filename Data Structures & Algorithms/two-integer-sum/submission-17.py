class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSorted = [(e, i) for i, e in enumerate(nums)]
        numsSorted.sort()
        l, r = 0, len(numsSorted)-1
        while l < r:
            sumLR = numsSorted[l][0] + numsSorted[r][0]
            if sumLR == target:
                return [min(numsSorted[l][1], numsSorted[r][1]), max(numsSorted[l][1], numsSorted[r][1])]
            elif sumLR < target:
                l += 1
            else:
                r -= 1                