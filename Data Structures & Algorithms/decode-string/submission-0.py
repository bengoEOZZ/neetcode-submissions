class Solution:
    def decodeString(self, s: str) -> str:
        stringStack = []
        numStack = []
        curr = ""
        currNum = 0

        for c in s:
            if c.isdigit():
                currNum = currNum*10 + int(c)
            elif c == '[':
                stringStack.append(curr)
                numStack.append(currNum)
                curr = ""
                currNum = 0
            elif c == ']':
                prevStr = stringStack.pop()
                num = numStack.pop()
                curr = prevStr + (curr*num)
            else:
                curr += c
        return curr