class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSorted = []
        for i, e in enumerate(nums):
            numsSorted.append((e,i))
        numsSorted.sort()

        l, r = 0, len(nums)-1
        while l < r:
            sumLR = numsSorted[l][0] + numsSorted[r][0]
            if sumLR == target:
                return [min(numsSorted[l][1],numsSorted[r][1]), max(numsSorted[l][1],numsSorted[r][1])]
            elif sumLR < target:
                l += 1
            else:
                r -= 1