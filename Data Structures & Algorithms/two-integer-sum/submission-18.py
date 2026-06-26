class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, e in enumerate(nums):
            diff = target - e
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[e] = i