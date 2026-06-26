class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for e in nums:
            if e not in frequencies:
                frequencies[e] = 1
            else:
                frequencies[e] += 1
        sortedFrequencies = []
        for e, freq in frequencies.items():
            sortedFrequencies.append((freq, e))
        sortedFrequencies.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(sortedFrequencies[i][1])
        return ans