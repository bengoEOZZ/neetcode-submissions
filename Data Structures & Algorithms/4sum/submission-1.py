class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > target and nums[i] > 0:
                    return ans
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1
                while l < r:
                    sumAll = nums[i] + nums[j] + nums[l] + nums[r]
                    if sumAll == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif sumAll < target:
                        l += 1
                    else:
                        r -= 1
        return ans