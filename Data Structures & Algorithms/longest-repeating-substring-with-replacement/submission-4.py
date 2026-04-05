class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        max_f = 0
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            max_f = max(max_f, freq[ch])
            if (r - l + 1) - max_f > k:
                l+=1
                freq[s[l]]-=1
        return r - l + 1

        