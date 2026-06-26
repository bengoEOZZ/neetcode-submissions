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
        if zeroCount == 1:
            ans[nums.index(0)] = productNoZero
            return ans
        for i, n in enumerate(nums):
            ans[i] = productAll//n
        return ans