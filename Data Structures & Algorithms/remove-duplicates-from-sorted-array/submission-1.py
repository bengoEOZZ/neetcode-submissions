class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums[curr] = nums[i]
            curr += 1
        return curr