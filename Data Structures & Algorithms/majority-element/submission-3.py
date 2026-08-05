class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countN = {}
        for n in nums:
            countN[n] = countN.get(n, 0) + 1
            if countN[n] > len(nums)//2:
                return n