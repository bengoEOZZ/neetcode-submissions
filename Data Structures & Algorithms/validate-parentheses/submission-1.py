class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', '}': '{', ']': '['}
        print(parentheses.values())
        for b in s:
            if b in parentheses:
                if stack and stack[-1] == parentheses[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False