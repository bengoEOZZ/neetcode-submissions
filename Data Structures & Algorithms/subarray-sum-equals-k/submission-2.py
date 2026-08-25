class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        rSum, ans = 0, 0
        for n in nums:
            rSum += n
            # rSum - lSum = k
            # lSum = rSum - k
            lSum = rSum - k
            if lSum in prefix:
                ans += prefix[lSum]
            prefix[rSum] += 1
        return ans