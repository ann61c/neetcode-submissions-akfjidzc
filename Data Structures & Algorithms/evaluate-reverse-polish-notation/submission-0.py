class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif c == "/":
                a, b = int(float(stack.pop)), int(float(stack.pop))
                stack.append(a / b)
            else:
                stack.append(int(c))
        return stack[0]
        