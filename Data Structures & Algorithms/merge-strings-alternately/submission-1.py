class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            ans += word1[i] + word2[i]
        ans += word1[minLength:] if len(word1) >= len(word2) else word2[minLength:]
        return ans