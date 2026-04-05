class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = {}
        for ch in t:
            count[ch] = count.get(ch, 0) + 1
        find = {}
        for r, ch in enumerate(s):
            if ch in count:
                count[ch]-=1
                if ch not in find:
                    find[ch] = r
                else:
                    find[ch] = max(r, find[ch])
        start = min(find.values())
        end = max(find.values())
        return s[start:end+1]

