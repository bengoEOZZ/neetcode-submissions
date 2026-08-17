class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rSum, ans = 0, 0
        prefix = { 0:1 }
        for n in nums:
            rSum += n
            # rSum - lSum = k
            # lSum = rSum - k
            lSum = rSum - k
            if lSum in prefix:
                ans += prefix[lSum]
            prefix[rSum] = prefix.get(rSum, 0) + 1
        return ans