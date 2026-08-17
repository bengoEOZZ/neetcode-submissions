class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, accSum = 0, 0
        prefix = { 0:1 }
        for n in nums:
            accSum += n
            diff = accSum-k
            if diff in prefix:
                ans += prefix[diff]
            prefix[accSum] = prefix.get(accSum, 0) + 1
        return ans