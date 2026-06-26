class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in parentheses.values():
                stack.append(b)
            elif stack and stack[-1] == parentheses[b]:
                stack.pop()
            else:
                return False
        return True if not stack else False