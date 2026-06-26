class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for e in nums:
            if e not in frequency:
                frequency[e] = 1
            else:
                frequency[e] += 1
        frequencySorted = []
        for e in frequency:
            frequencySorted.append((frequency[e], e))
        frequencySorted.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(frequencySorted[i][1])
        return ans