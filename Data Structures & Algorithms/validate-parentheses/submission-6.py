class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(', ']':'[', '}':'{'}
        
        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0 and ch != close_to_open[stack[-1]]:
                    return False
                stack.pop()
            
        return True if len(stack) == 0 else False
            

            
            