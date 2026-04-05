class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_other = {}
        trusted = {}
        for pair in trust:
            trust_other[pair[0]] = trust_other.get(pair[0], 0) + 1
            trusted[pair[1]] = trusted.get(pair[1], 0) + 1
        # highest = 0
        # for people in trusted:
        #     highest = max(highest, trusted[people])
        # print(highest)
        for i in range(1, n):
            # if i not in trusted and highest == n - 1:
            if trusted.get(i, 0) == n - 1 and i not in trust_other:
                return i
        return -1