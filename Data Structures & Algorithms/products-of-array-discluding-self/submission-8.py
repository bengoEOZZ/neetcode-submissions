class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAll, productNoZero, zeroCount = 1, 1, 0
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                productNoZero *= n
            productAll *= n
        ans = [0]*len(nums)
        if zeroCount > 1:
            return ans
        for i, n in enumerate(nums):
            if n == 0 and zeroCount == 1:
                ans[i] = productNoZero
            else:
                ans[i] = productAll//n
        return ans