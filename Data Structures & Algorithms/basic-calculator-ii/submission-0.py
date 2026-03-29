class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = s + "+"
        last_op = "+"
        number = 0
        res = 0
        stack = []
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            else:
                if last_op == "+":
                    stack.append(number)
                elif last_op == "-":
                    stack.append(number * (-1))
                elif last_op == "*":
                    prev = stack.pop() * number
                    stack.append(prev)
                elif last_op == "/":
                    prev = int(stack.pop() / number)
                    stack.append(prev)
                last_op = ch
                number = 0
        return sum(stack)
        