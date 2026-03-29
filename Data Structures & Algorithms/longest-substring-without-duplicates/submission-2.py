class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sus_map = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in sus_map and sus_map[char] >= left:
                left = sus_map[char] + 1
            
            sus_map[char] = right
            max_len = max(right - left + 1, max_len)
        return max_len

        
        