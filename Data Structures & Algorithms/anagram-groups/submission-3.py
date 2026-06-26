class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for s in strs:
            count = [0]*26
            for c in s:
                count[alpha.index(c)] += 1
            count = tuple(count)
            if count not in ans:
                ans[count] = [s]
            else:
                ans[count].append(s)
        return ans.values()