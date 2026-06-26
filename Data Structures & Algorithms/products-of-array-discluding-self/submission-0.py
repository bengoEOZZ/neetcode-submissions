class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAll, productNoZero, zeroCount = 1, 1, 0
        for e in nums:
            productAll *= e
            if e == 0:
                zeroCount += 1
            else:
                productNoZero *= e
        productExceptSelf = []
        print(productAll)
        for e in nums:
            if e == 0:
                if zeroCount == 1:
                    productExceptSelf.append(productNoZero)
                else:
                    productExceptSelf.append(productAll)
            else:
                productExceptSelf.append(productAll//e)
        return productExceptSelf