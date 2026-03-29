class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        p = []
            
        def isPalindrome(s):
            left = 0
            right = len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1
            return True
        
        def dfs(index):
            if index == len(s):
                res.append(p.copy())
            for i in range(index, len(s)):
                part = s[index:i+1]
                if isPalindrome(part):
                    p.append(part)
                    dfs(i+1)
                    p.pop()
        dfs(0)
        return res

