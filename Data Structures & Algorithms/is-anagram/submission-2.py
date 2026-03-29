class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        compare = {}
        compare_2 = {}
        for ch in s:
            compare[ch] = compare.get(ch, 0) + 1
        for ch in t:
            compare_2[ch] = compare_2.get(ch, 0) + 1
        return compare == compare_2
        
