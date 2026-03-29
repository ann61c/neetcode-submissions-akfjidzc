class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_1 = {}
        window_map = {}
        for s in s1:
            if not s in freq_1:
                freq_1[s] = 1
            else:
                freq_1[s] += 1

        # for s in s2:
        for i in range(len(s1)):
            s = s2[i]
            if not s in window_map:
                window_map[s] = 1
            else:
                window_map[s] += 1
        if window_map == freq_1:
            return True


        for i in range(len(s1), len(s2)):
            if not s2[i] in window_map:
                window_map[s2[i]] = 1
            else:
                window_map[s2[i]] += 1
            
            old = s2[i - len(s1)]
            window_map[old] -= 1

            if window_map[old] == 0:
                del window_map[old]
            
            if window_map == freq_1:
                return True


        print(freq_1)
        print(window_map)
        return False