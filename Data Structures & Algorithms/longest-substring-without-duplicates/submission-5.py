class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dup = {}
        longest = 0
        for r, ch in enumerate(s):
            if ch not in dup:
                dup[ch] = r
            else:
                l = r 
                dup[ch] = r
            longest = max(longest, r - l)
        return longest + 1



