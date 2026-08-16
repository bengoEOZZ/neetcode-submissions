class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}
        ans = set()
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
            if hashMap[n] > (len(nums)//3):
                ans.add(n)
        return list(ans)