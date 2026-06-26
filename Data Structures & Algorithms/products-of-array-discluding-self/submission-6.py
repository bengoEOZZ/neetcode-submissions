class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAll, productNoZero, zeroCount = 1, 1, 0
        for e in nums:
            productAll *= e
            if e == 0:
                zeroCount += 1
            else:
                productNoZero *= e
        ans = []
        if zeroCount > 1:
            return [0] * len(nums)
        for e in nums:
            if e == 0:
                ans.append(productNoZero)
            else:
                ans.append(productAll//e)
        return ans