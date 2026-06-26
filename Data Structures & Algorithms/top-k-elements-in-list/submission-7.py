class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n] += 1
        frequencySorted = [(freq, n) for n, freq in frequency.items()]
        frequencySorted.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(frequencySorted[i][1])
        return ans