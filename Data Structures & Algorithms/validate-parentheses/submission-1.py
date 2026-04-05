class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, ch in enumerate(s):
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            else:
                chara = stack.pop()
                if (ch == '[' and chara == ']') or (ch == '{' and chara == '}') or (ch == '[' and chara == ']'):
                    continue
                else:
                    return True
        return False