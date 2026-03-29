class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                while stack and t > temperatures[stack[-1]]:
                    last_day = stack.pop()
                    res[last_day] = i - last_day
                stack.append(i)
        return res

                    
