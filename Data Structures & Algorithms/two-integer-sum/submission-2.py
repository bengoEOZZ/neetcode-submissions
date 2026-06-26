class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = [] #[[5,0], [2,1], [3,2], [0,3], [4,4]]
        for i, e in enumerate(nums):
            sortedNums.append([e, i])
        sortedNums.sort()
        print(sortedNums)
        l, r = 0, len(sortedNums)-1
        while l < r:
            summed = sortedNums[l][0] + sortedNums[r][0]
            if summed < target:
                l += 1
            elif summed > target:
                r -= 1
            else:
                return [min(sortedNums[l][1],sortedNums[r][1]), max(sortedNums[l][1],sortedNums[r][1])]