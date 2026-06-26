class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for e in nums:
            if e not in frequency:
                frequency[e] = 1
            else:
                frequency[e] += 1
        numsSorted = []
        for e, freq in frequency.items():
            numsSorted.append((freq, e))
        numsSorted.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(numsSorted[i][1])
        return ans