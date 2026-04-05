class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []

        for i, ch in enumerate(s):
            if stack and ch in pairs:
                part = stack[-1]
                if part == pairs[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True
