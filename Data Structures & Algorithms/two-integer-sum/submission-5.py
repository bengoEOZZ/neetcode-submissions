class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, e in enumerate(nums):
            difference = target - e
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[e] = i