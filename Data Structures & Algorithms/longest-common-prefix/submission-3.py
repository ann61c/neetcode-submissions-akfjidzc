class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, char in enumerate(strs[0]):
            for s in strs:
                if len(s) <= i:
                    return strs[0][:i]
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
                