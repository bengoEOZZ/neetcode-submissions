class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length = 0
            while s[i].isdigit():
                length = length*10 + int(s[i])
                i += 1
            i += 1
            ans.append(s[i:i+length])
            i = i+length
        return ans