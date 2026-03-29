class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(', ']':'[', '}':'{'}
        
        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if close_to_open[ch] != stack.pop():
                    return False
            
        return len(stack) == 0
            

            
            