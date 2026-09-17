class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashSet = set()
        k = 0
        for i, n in enumerate(nums):
            if n not in hashSet:
                nums[k] = n
                k += 1
            hashSet.add(n)
        return k