class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for e in nums:
            if e in hashSet:
                return True
            hashSet.add(e)
        return False