class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token1) + int(token2))
            elif token == '-':
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token2) - int(token1))
            elif token == '*':
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token1) * int(token2))
            elif token == '/':
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token2) / int(token1))
            else:
                stack.append(int(token))
        return stack[-1]