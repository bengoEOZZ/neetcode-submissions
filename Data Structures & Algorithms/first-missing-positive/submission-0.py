class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # --- PLACE EACH VALUE AT ITS "CORRECT" INDEX (v -> index v-1) ---
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                homeIndex = nums[i] - 1
                nums[i], nums[homeIndex] = nums[homeIndex], nums[i]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1