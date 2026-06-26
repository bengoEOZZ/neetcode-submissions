class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAll, productWithoutZero, zeroCount = 1, 1, 0
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                productWithoutZero *= n
            productAll *= n
        ans = [0] * len(nums)
        if zeroCount > 1:
            return ans
        for i, n in enumerate(nums):
            if n == 0:
                ans[i] = productWithoutZero
            else:
                ans[i] = (productAll//n)
        return ans