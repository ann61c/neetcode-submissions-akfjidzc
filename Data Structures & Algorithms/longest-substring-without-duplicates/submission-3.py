class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chara = {}
        l = 0
        res = 0
        #index, character
        for i, r in enumerate(s):
            if r in chara:
                l = i 
            elif r not in chara:
                chara[r] = i
            res = max(res, i - l + 1)
        return res