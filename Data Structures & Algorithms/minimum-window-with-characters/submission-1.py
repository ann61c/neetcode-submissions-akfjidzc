class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        need = len(target)
        
        l = 0
        have = 0
        window = {}
        res_len = float('inf')
        res_start = 0
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if window[ch] == target[ch]:
                have +=1
            while l <= r and need == have:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res_start = l
                if s[l] in target and window[s[l]] == target[s[l]]:
                    have -=1
                window[s[l]]-=1
                l+=1
        return "" if len(t) > len(s) else s[res_start:res_start + res_len]


