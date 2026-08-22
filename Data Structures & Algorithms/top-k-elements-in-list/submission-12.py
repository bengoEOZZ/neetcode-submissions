class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        for n, freq in count.items():
            buckets[freq].append(n)
        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans