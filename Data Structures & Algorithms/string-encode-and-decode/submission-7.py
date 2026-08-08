class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString = encodedString + str(len(s)) + "#" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        i, ans = 0, []
        while i < len(s):
            length = ""
            curr = i
            while s[curr] != '#':
                length += s[curr]
                curr += 1
            ans.append(s[curr+1:curr+1+int(length)])
            i = curr + 1 + int(length)
        return ans