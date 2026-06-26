class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + '#' + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString, i = [], 0
        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            decodedString.append(s[i:i+int(length)])
            i += int(length)
        return decodedString