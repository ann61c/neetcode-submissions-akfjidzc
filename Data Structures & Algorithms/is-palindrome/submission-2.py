class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for i in range(len(s)):
            if s[i].isalnum():
                text+=s[i].lower()
        left = 0
        right = len(text) - 1
        while left <= right:
            if text[left] != text[right]:
                return False
            left+=1
            right-=1
        return True