class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "#" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings, i = [], 0
        print(s)
        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            decodedStrings.append(s[i+1:i+1+int(length)])
            i += 1+int(length)
        return decodedStrings