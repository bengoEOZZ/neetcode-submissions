class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr, i = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
            i += 1
        return curr