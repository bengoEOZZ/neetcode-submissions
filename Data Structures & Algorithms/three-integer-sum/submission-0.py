class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # No combination can equal to 0, all positive numbers
            if n > 0:
                break
            
            l, r = i+1, len(nums)-1
            while l < r:
                sumLR = n + nums[l] + nums[r]
                if sumLR > 0:
                    r -= 1
                elif sumLR < 0:
                    l += 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return ans