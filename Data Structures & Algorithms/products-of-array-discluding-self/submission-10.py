class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1]*len(nums)
        prefixProduct[0] = nums[0]
        suffixProduct = [1]*len(nums)
        suffixProduct[len(nums)-1] = nums[len(nums)-1]
        product = [1]*len(nums)
        
        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i]

        for i in range(len(nums)):
            prefix = prefixProduct[i-1] if i > 0 else 1
            suffix = suffixProduct[i+1] if i < len(nums)-1 else 1
            product[i] = prefix*suffix

        return product