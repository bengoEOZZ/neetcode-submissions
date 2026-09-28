class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans, path = [], []

        def NSum(n, start, target):
            if n == 2:
                l, r = start, len(nums)-1
                while l < r:
                    sumLR = nums[l] + nums[r]
                    if sumLR > target:
                        r -= 1
                    elif sumLR < target:
                        l += 1
                    else:
                        ans.append(path + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                return

            # Ensure at least n elements left
            # curr(i) + (n-1) < len(nums)
            # curr(i) < len(nums) -n +1
            for i in range(start, len(nums)-n+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                NSum(n-1, i+1, target-nums[i])
                path.pop()
        
        NSum(4, 0, target)
        return ans