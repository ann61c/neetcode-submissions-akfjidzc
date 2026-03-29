class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        strs = {}
        for i, ch in enumerate(s1):
            strs[ch] = strs.get(ch, 0) + 1
        
        left = 0
        strs2= {}
        
        for r, ch in enumerate(s2):
            strs2[ch] = strs2.get(ch, 0) + 1
            if r >= k:
                strs2[s2[r-k]]-=1
                if strs2[s2[r-k]] == 0:
                    del strs2[s2[r-k]]
            if strs2 == strs:
                return True
        return False