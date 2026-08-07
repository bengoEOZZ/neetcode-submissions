class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        heap = []
        for elem, freq in count.items():
            heapq.heappush(heap, (-freq, elem))
        
        ans = []
        for i in range(k):
            freq, elem = heapq.heappop(heap)
            ans.append(elem)

        return ans