class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return tokens[0]
        for token in tokens:
            if token.isdigit():
                stack.append(token)
            elif token == '+':
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token1) + int(token2))
            elif token == '-':
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token1) - int(token2))
            elif token == '*':
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token1) * int(token2))
            else:
                token1 = stack.pop()
                token2 = stack.pop()
                stack.append(int(token1) / int(token2))
        return stack[-1]