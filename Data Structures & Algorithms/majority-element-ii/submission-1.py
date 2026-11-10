class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        hashMap = defaultdict(int)
        for n in nums:
            hashMap[n] += 1
            if n not in ans and hashMap[n] > len(nums)//3:
                ans.append(n)
        return ans